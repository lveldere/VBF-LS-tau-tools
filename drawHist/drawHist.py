#!/usr/bin/env python
# TODO: read default style options from cfg
# TODO: sanity check: trace recursive dependencies

import sys,ConfigParser,os,shutil
import ROOT as rt
import mytools

DEBUG = False
TEXTFONT=44
TEXTSIZE_BIG=30
TEXTSIZE_SMALL=25
YTITLEOFFSET=1.4
XTITLEOFFSET=1.4
CANVASWIDTH=800
CANVASHEIGHT=800
FRACRATIO=0.22

#############################
# read command line options
#############################

from optparse import OptionParser
parser = OptionParser()
parser.add_option("--drawrules",dest="drawrules",default="drawRules.cfg",help="path to cfg file with draw rules, default=[%default]")
parser.add_option("--idir",dest="idir",default="input_weighted",help="path to directory with input histogram files, default=[%default]")
parser.add_option("--odir",dest="odir",help="path to output directory, default=IDIR_drawn")
parser.add_option("--force",dest="force",action="store_true",default=False,help="if ODIR already exists, override, default=%default")
parser.add_option("--oformat",dest="oformat",default="pdf",help="output format, default=[%default]")
parser.add_option("--histpath",dest="histpath",help="paths to histograms/directories to be drawn, default: all histograms in all directories are drawn")
parser.add_option("--histcfg",dest="histcfg",help="cfg for histograms, e.g. to set x and ytitles")
parser.add_option("--verbose",dest="verbose",action="store",help="run in verbose mode",default=0)
(options, args) = parser.parse_args()
if options.odir == None:
    options.odir = options.idir.rstrip("/") + "_drawn"
# get rid of root gui
sys.argv.append("-b")

#############################
# define canvasses
#############################
CANVAS = rt.TCanvas("c1","c1",CANVASWIDTH,CANVASHEIGHT)
CANVAS.SetTopMargin(0.08)
HISTPAD = rt.TPad("histpad","histpad",0.,FRACRATIO,1.,1.)
HISTPAD.SetTopMargin(float(TEXTSIZE_BIG)*2/CANVASHEIGHT/(1-FRACRATIO))
HISTPAD.SetLeftMargin(0.12)
HISTPAD.SetBottomMargin(0.13)
HISTPAD.SetRightMargin(0.05)
CANVAS.cd()
HISTPAD.Draw()
RATIOPAD = rt.TPad("ratiopad","ratiopad",0.,0.,1.,FRACRATIO)
RATIOPAD.SetLeftMargin(0.12)
RATIOPAD.SetRightMargin(0.05)
RATIOPAD.SetTopMargin(0.013/(FRACRATIO))
RATIOPAD.SetBottomMargin(0.05/(FRACRATIO))
RATIOPAD.SetTicks(1,1)
CANVAS.cd()
RATIOPAD.Draw()
#######################
# given a key, gets value from dictionary
# if key is not available:
#  - set default values
#  - print warnings/errors for missing keys
#######################  
def myGet(key,_dict,default=None,dictName="",warnIfMissing=False,exitIfMissing=False):
    if key in _dict:
        return _dict[key]
    if not warnIfMissing and not exitIfMissing:
        return default
    msg = ""
    if dictName != "":
        msg = " in " + dictName + " "
    if warnIfMissing:
        print "WARNING: no key '{0}'{1}, returning default, {2}.".format(key,msg,str(default))
        return default
    if exitIfMissing:
        print "ERROR: no key '{0}'{1}, exit...".format(key,msg)
        sys.exit()

########################
# converts list of pairs into dictionary
#######################
def listOfPairs2Dict(list):
    return dict([[x,y] for x,y in list])

#######################
# bookkeep histogram style
#######################
class MyHistStyle:
    def __init__(self,name,options):
        self.name = name
        self.lineColor = int(myGet("line color",options,rt.kBlack))
        self.fillStyle = int(myGet("fill style",options,1001))
        self.fillColor = int(myGet("fill color",options,0))
        self.markerStyle = int(myGet("marker style",options,0))
        self.markerColor = int(myGet("marker color",options,1))
        self.drawOption = myGet("draw option",options,"")
        self.legendTitle = myGet("legend title",options,"")
        self.legendOption = myGet("legend option",options,"l")

    def apply(self,hist):
        if hist == None:
            return
        # style histograms
        xaxis = None
        yaxis = None
        if hist.InheritsFrom("TH1"):
            if self.lineColor is not None: hist.SetLineColor(self.lineColor)
            if self.fillStyle is not None: hist.SetFillStyle(self.fillStyle)
            if self.fillColor is not None: hist.SetFillColor(self.fillColor)
            if self.markerStyle is not None: hist.SetMarkerStyle(self.markerStyle)
            if self.markerColor is not None: hist.SetMarkerColor(self.markerColor)
            xaxis = hist.GetXaxis()
            yaxis = hist.GetYaxis()
            hist.SetStats(0)
            hist.SetTitle("")
        elif hist.InheritsFrom("THStack"):
            xaxis = hist.GetHistogram().GetXaxis()
            yaxis = hist.GetHistogram().GetYaxis()
        # style axes
        yaxis.SetLabelFont(TEXTFONT)
        yaxis.SetLabelSize(TEXTSIZE_SMALL)
        yaxis.SetTitleOffset(YTITLEOFFSET)
        yaxis.CenterTitle()
        yaxis.SetTitleFont(TEXTFONT)
        yaxis.SetTitleSize(TEXTSIZE_BIG)
        xaxis.SetLabelFont(TEXTFONT)
        xaxis.SetLabelSize(TEXTSIZE_SMALL)
        xaxis.SetTitleOffset(XTITLEOFFSET)
        xaxis.CenterTitle()
        xaxis.SetTitleFont(TEXTFONT)
        xaxis.SetTitleSize(TEXTSIZE_BIG)
        xaxis.SetTickLength(0.02/(1.-FRACRATIO))
        yaxis.SetTickLength(0.02)
        yaxis.SetLabelOffset(0.002/(1.-FRACRATIO))

#######################
# style specific for ratios
#######################
def applyRatioStyle(hist):
    if hist == None:
        return
    hist.SetMinimum(0)
    hist.SetMaximum(2)
    hist.SetLabelSize(0,"X")
    hist.GetXaxis().SetTickLength(0.02/FRACRATIO)
    hist.GetXaxis().SetLabelOffset(0.05/FRACRATIO)
    hist.GetYaxis().SetNdivisions(3,5,0)
    hist.GetYaxis().SetTickLength(0.02)
    hist.GetYaxis().SetLabelOffset(0.002/FRACRATIO)


#######################
# Draw rules for histograms
#######################
class DrawRuleHist:
    def __init__(self,name,options):
        self.name = name
        self.fileNames = myGet("files",options,dictName=name,exitIfMissing=True).split(",")
        if len(self.fileNames)==0:
            print "ERROR in DrawRuleHist.__init__: 0 files, exit"
            sys.exit()
        self.fileNames = [fileName + ".root" for fileName in self.fileNames] 
        self.histStyle = MyHistStyle(name,options)
        self.filePaths = None
        self.files = None
        self.hist = None 
        self._hists = None
        self._init = False
        self.up2data = False
        
    def init(self,idir,rules):
        if not self._init:
            self.files = [rt.TFile.Open(idir + "/" + fileName) for fileName in self.fileNames]
            for _file in self.files:
                paths = mytools.listRootFile(_file)
                for p in paths:
                    _file.Get(p)
            for f in range(0,len(self.files)):
                _file = self.files[f]
                if _file == None:
                    print "WARNING: skipping file",self.fileNames[f]
                    continue
            self._init = True

    def reset(self):
        self.hist = None
        self.up2date = False
        
    def updateHist(self,histPath):
        if self.up2date:
            if options.verbose > 1:
                print "already up to date"
            return
        if options.verbose > 1:
            print "updating"
        self.up2date = True

        if not self._init:
            print "ERROR: call init before calling updateHist, exit..."
            sys.exit()

        for f in range(0,len(self.files)):
            _file = self.files[f]
            if _file == None:
                continue
            obj = _file.Get(histPath)
            if options.verbose:
                print "   " + _file.GetName()
            if obj == None:
                print "WARNING: no histogram named \"" + histPath + "\"in file \"" + _file.GetName() + ", skipping..."
                continue
            if options.verbose > 1:
                if obj.GetXaxis().GetLabels() != None:
                    print [x for x in obj.GetXaxis().GetLabels()]
            if self.hist is None:
                self.hist = obj.Clone()
            else:
                self.hist.Add(obj)

        self.histStyle.apply(self.hist)

#######################
# Draw rules for histogram sums
#######################
class DrawRuleHistSum:
    def __init__(self,name,options):
        self.name = name
        self.histNames = myGet("hists",options,dictName=name,exitIfMissing=True).split(",")
        self.histStyle = MyHistStyle(name,options)
        self.hist = None
        self.drawRules = None
        self._init = False
        self.up2date = False

    def init(self,idir,rules):
        if not self._init:
            self.drawRules = [rules[histName] for histName in self.histNames] 
            self._init = True

    def reset(self):
        self.hist = None
        self.up2date = False
    
    def updateHist(self,histPath):
        if self.up2date:
            return
        self.up2date = True

        if not self._init:
            print "ERROR: call init before calling updateHist, exit..."
            sys.exit()

        for rule in self.drawRules:
            if options.verbose:
                print "   " + rule.name
            rule.updateHist(histPath)
            if rule.hist == None:
                continue
            if self.hist is None:
                self.hist = rule.hist.Clone()
            else:
                self.hist.Add(rule.hist.Clone())
        self.histStyle.apply(self.hist)
        
#######################
# Draw rules for histogram stack
#######################
class DrawRuleHistStack:
    def __init__(self,name,options):
        self.name = name
        self.histNames = myGet("hists",options,dictName="section '" + name + "'",exitIfMissing=True).split(",")
        self.histStyle = MyHistStyle(name,options)
        self.currentxtitle = ""
        self.currentytitle = ""
        self._init = False
        self.drawRules = None
        self.up2date = False

    def init(self,idir,rules):
        if not self._init:
            self.drawRules = [rules[histName] for histName in self.histNames] 
            self._init = True

    def reset(self):
        self.hist = None
        self.up2date = False
                                      
    def updateHist(self,histPath):
        if self.up2date:
            return
        self.up2date = True

        if not self._init:
            print "ERROR: call init before calling updateHist, exit..."
            sys.exit()

        for rule in self.drawRules:
            if options.verbose:
                print "   " + rule.name
            rule.updateHist(histPath)
            if rule.hist == None:
                continue
            if self.hist is None:
                self.hist = rt.THStack("stack","")
                self.currentxtitle = rule.hist.GetXaxis().GetTitle()
                self.currentytitle = rule.hist.GetYaxis().GetTitle()
                self.hist.SetName(rule.hist.GetName())
            self.hist.Add(rule.hist)
        # !!! APPLY STACK STYLE AFTER DRAWING
        #self.histStyle.apply(self.hist)

        #if DEBUG:
        #    print "updated DrawRulHistStack " + self.name + ", hist:",self.hist 

#######################
# Draw rules for histogram ratios
#######################
class DrawRuleHistRatio:
    def __init__(self,name,options):
        self.name = name
        self.numeratorHistName = myGet("numerator hist",options,dictName="section '" + name + "'",exitIfMissing=True)
        self.denominatorHistName = myGet("denominator hist",options,dictName="section " + name + "'",exitIfMissing=True)
        nonRefOptions = dict()
        refOptions = dict()
        for key in options:
            if key.find("ref") !=0:
                nonRefOptions.update([[key,options[key]]])
            else:
                _key = key.replace("ref ","")
                refOptions.update([[_key,options[key]]])
        self.histStyle = MyHistStyle(name,nonRefOptions)
        self.refHistStyle = MyHistStyle(name,refOptions)
        self.hist = None
        self.refHist = None
        self.refHist2 = None
        self.numeratorDrawRule = None
        self.denominatorDrawRule = None
        self.numeratorHist = None
        self.denominatorHist = None
        self._init = False
        self.drawRef = bool(myGet("draw ref",options,default=0))
        self.up2date = False

    def reset(self):
        self.hist = None
        self.refhist = None
        self.up2date = False

    def init(self,idir,rules):
        if not self._init:
            self.numeratorDrawRule = rules[self.numeratorHistName] 
            self.denominatorDrawRule = rules[self.denominatorHistName] 
            self._init = True 

    def updateHist(self,histPath):
        if self.up2date:
            return
        self.up2date = True

        if not self._init:
            print "ERROR: call init before calling updateHist, exit..."
            sys.exit()

        self.numeratorDrawRule.updateHist(histPath)
        self.denominatorDrawRule.updateHist(histPath)
        if self.numeratorDrawRule.hist == None:
            return
        if self.denominatorDrawRule.hist == None:
            return

        # the ratio
        self.hist = self.numeratorDrawRule.hist.Clone()
        temp = self.denominatorDrawRule.hist.Clone()
        for b in range(0,temp.GetNbinsX()+1):
            temp.SetBinError(b,0.)
        self.hist.Divide(temp)
        self.histStyle.apply(self.hist)

        # the reference
        self.refHist = self.denominatorDrawRule.hist.Clone()
        self.refHist.Divide(temp)
        for b in range(1,self.refHist.GetNbinsX()+1):
            self.refHist.SetBinContent(b,1)
        self.refHistStyle.apply(self.refHist)
        self.refHist2 = self.refHist.Clone()
        self.refHist2.SetFillStyle(0)
        



        
#######################
# Book keep main draw rule options
#######################
class DrawRules:
    def __init__(self,cfgPath):

        # declare member variables
        self._draw = []
        self.drawratio = None
        self.title = None
        self.rules = dict()
        self.idir = ""
        self.odir = ""
        self.force = False
        self.filesOpen = False
        self._init = False
        self.defaultYtitle = None
        self.drawLegend = None
        
        # read cfg file
        cfg = ConfigParser.RawConfigParser()
        cfg.read(cfgPath)
        
        # parse main cfg section
        mainOptions = listOfPairs2Dict(cfg.items("main"))
        dictName = "section 'main'"
        self._draw = myGet("draw",mainOptions,dictName=dictName,exitIfMissing=True).split(",")
        self.drawratio = myGet("drawratio",mainOptions,dictName=dictName,default=None)
        if self.drawratio is not None:
            self.drawratio = self.drawratio.split(",")
        self.title = myGet("title",mainOptions,dictName=dictName,default=None) 
        self.ytitle = myGet("ytitle",mainOptions,default="events per bin")    
        self.histCfgPath = None 
        self.histCfg = None
        self.drawlegend = int(myGet("drawlegend",mainOptions,default="1"))

        # parse other sections
        for section in cfg.sections():
            if section=="main":
                continue
            _options = listOfPairs2Dict(cfg.items(section))
            # sections should be named [type name]
            type,name=section.split()
            drawRule = None
            if type == "Hist":
                drawRule = DrawRuleHist(section,_options)
            elif type == "HistSum":
                drawRule = DrawRuleHistSum(section,_options)
            elif type == "HistStack":
                drawRule = DrawRuleHistStack(section,_options)
            elif type == "HistRatio":
                drawRule = DrawRuleHistRatio(section,_options)
            else:
                print "ERROR: unknown type of draw rule",type
                sys.exit()
            self.rules.update([[name,drawRule]])
        
        # consistent draw rules?
        if len(self.rules)==0:
            print "ERROR: now draw rules defined, exit"
            sys.exit()

    def init(self):
        # init each draw rule
        if self._init:
            return
        self._init = True
        for rule in self.rules.values():
            rule.init(self.idir,self.rules)

        # create output directory
        if os.path.exists(self.odir):
            if self.force:
                shutil.rmtree(self.odir)
            else:
                print "ERROR: ODIR already exists, use option --force to override"
                sys.exit()
        os.mkdir(self.odir)

        # read in plot cfg
        if self.histCfgPath:
            print "reading in plot cfg from",self.histCfgPath
            self.histCfg = ConfigParser.RawConfigParser()
            self.histCfg.read(self.histCfgPath)
            if  self.histCfg.has_section("default"):
                options = listOfPairs2Dict(self.histCfg.items("default"))
                self.defaultYtitle = myGet("ytitle",options,"events per bin")

    def getHistPaths(self,base=""):
        print "reading histogram paths ..."
        self.init()
        templateFile = None
        for rule in self.rules.values():
            if isinstance(rule,DrawRuleHist):
                for f in range(0,len(rule.files)):
                    if rule.files[f] != None:
                        print "reading histogram paths from " + rule.files[f].GetName()
                        templateFile = rule.files[f]
                        break
                if templateFile != None:
                    break
        paths = mytools.listRootFile(templateFile,base)
        for p in reversed(range(0,len(paths))):
            o = templateFile.Get(paths[p])
            if not o.ClassName() == "TH1D" and not o.ClassName() == "TH1F":
                del paths[p]
        return paths

    def resetHist(self):
        for rule in self.rules.values():
            rule.reset()

    def updateHist(self,histpath):
        if DEBUG:
            print "update all histograms"
        self.init()
        self.resetHist()
        for rule in self.rules.values():
            rule.updateHist(histpath)

    def applyHistCfg(self,hist):
        if self.histCfg is None:
            return
        if self.histCfg.has_section(hist.GetName()):
            options = listOfPairs2Dict(self.histCfg.items(hist.GetName()))
            xtitle = myGet("xtitle",options,default=None)
            ytitle = myGet("ytitle",options,default=None)
            if xtitle is not None:
                hist.GetXaxis().SetTitle(xtitle)
            if ytitle is not None:
                hist.GetYaxis().SetTitle(ytitle)
            elif self.defaultYtitle is not None:
                hist.GetYaxis().SetTitle(self.defaultYtitle)
            
    def draw(self,histpath):
        self.init()

        if options.verbose > 1:
            print "drawing histogram",histpath

        # read in the relevant histogram from each of the root files
        self.updateHist(histPath)

        # find and set max
        max = None
        for d in range(0,len(self._draw)):
            if self.rules[self._draw[d]].hist == None:
                continue
            _max = self.rules[self._draw[d]].hist.GetMaximum()
            if max == None or _max > max:
                max = _max

        # draw histograms
        HISTPAD.cd()
        nd = 0    #number of hist drawn
        for d in range(0,len(self._draw)):
            rule = self.rules[self._draw[d]]
            if rule.hist == None:
                if verbose > 1:
                    print "skip drawing for rule",rule.name
                continue
            nd += 1
            
            drawOption = rule.histStyle.drawOption
            if nd == 1:
                rule.hist.SetMaximum(max*1.1)
            if nd > 1:
                if drawOption == "":
                    drawOption = "SAME"
                else:
                    drawOption += ",SAME"
            if options.verbose > 1:
                print "   draw " + rule.name + " with draw option ", drawOption
            rule.hist.Draw(drawOption)
            self.applyHistCfg(rule.hist)
            
        # create and draw legend
        if self.drawlegend:
            legend = rt.TLegend(0.65,0.5,0.9,0.9)
            legend.SetBorderSize(0)
            legend.SetFillStyle(0)
            legend.SetTextAlign(12)
            legend.SetTextFont(TEXTFONT)
            legend.SetTextSize(TEXTSIZE_BIG)
            n = 0
            for d in range(0,len(self._draw)):
                rule = self.rules[self._draw[d]]
                if isinstance(rule,DrawRuleHistStack):
                    for _rule in reversed(rule.drawRules):
                        legend.AddEntry(_rule.hist,_rule.histStyle.legendTitle,_rule.histStyle.legendOption)
                        n+=1
                else:            
                    legend.AddEntry(rule.hist,rule.histStyle.legendTitle,rule.histStyle.legendOption)
                    n += 1
            legend.SetY1(0.9-float(n*TEXTSIZE_BIG*1.1)/CANVASHEIGHT/(1-FRACRATIO))
            legend.Draw()
        
        # a title on top
        pt = None
        if self.title is not None:
            pt = rt.TPaveText(.13,0.9,0.9,1.0,"NDC")
            pt.SetFillStyle(0)
            pt.SetBorderSize(0)
            tt = pt.AddText(self.title)
            tt.SetTextFont(TEXTFONT)
            tt.SetTextSize(TEXTSIZE_BIG)
            tt.SetTextAlign(22)
            pt.Draw()

        # bloody stacks
        for rule in self.rules.values():
            if isinstance(rule,DrawRuleHistStack):
                rule.histStyle.apply(rule.hist)
                HISTPAD.Update()
                HISTPAD.Modified()
                break

        # draw ratios
        if self.drawratio is not None:
            RATIOPAD.cd()
            nd = 0   # number of hist drawn
            for d in range(0,len(self.drawratio)):
                rule = self.rules[self.drawratio[d]]
                if rule.hist == None:
                    continue
                nd += 1
                # the ratio histogram
                drawOption = rule.histStyle.drawOption
                if nd > 1:
                    if drawOption == "":
                        drawOption = "SAME"
                    else:
                        drawOption += ",SAME"
                if nd==1:
                    applyRatioStyle(rule.hist)
                rule.hist.Draw(drawOption)
                # the reference histogram
                if rule.drawRef:
                    drawOption = rule.refHistStyle.drawOption
                    if drawOption == "":
                        drawOption = "SAME"
                    else:
                        drawOption += ",SAME"
                rule.refHist.Draw(drawOption)
                rule.refHist2.Draw("SAME,HIST")

        _opath = self.odir + "/" + histPath + "_lin." + self.oformat 
        _odir = os.path.split(_opath)[0]
        if not os.path.exists(_odir):
            os.makedirs(_odir)
        HISTPAD.SetLogy(0)
        if self.drawratio is None:
            HISTPAD.Print(_opath)
        else:
            CANVAS.Print(_opath)
        
        _opath = self.odir + "/" + histPath + "_log." + self.oformat 
        HISTPAD.SetLogy(1)
        if self.drawratio is None:
            HISTPAD.Print(_opath)
        else:
            CANVAS.Print(_opath)


##########################################################
##                                                      ##
## ########## ##########   #####   ########  ########## ##
## ##             ##      ##   ##  ##     ##     ##     ##
## ##             ##     ##     ## ##     ##     ##     ##
## ##########     ##     ######### ########      ##     ##
##         ##     ##     ##     ## ##     ##     ##     ##
##         ##     ##     ##     ## ##     ##     ##     ##
## ##########     ##     ##     ## ##     ##     ##     ##
##                                                      ##
##########################################################

############################
# read in draw rules from cfg
############################
print "read draw rules from",options.drawrules
drawRules = DrawRules(options.drawrules)
print "INPUT DIR: ",options.idir
drawRules.idir = options.idir
print "OUPUT DIR: ",options.odir
drawRules.odir = options.odir
drawRules.oformat = options.oformat
drawRules.force = options.force
if options.histcfg is not None:
    print "read hist cfg from",options.histcfg
drawRules.histCfgPath = options.histcfg

############################
# list histograms to be drawn
############################
if options.histpath is None:
    options.histpath = ""
histPaths = drawRules.getHistPaths(options.histpath)
if len(histPaths) == 0:
    print "WARNING: no histograms found!"

############################
# draw!
############################
nh = len(histPaths)
for h in range(nh):
    histPath = histPaths[h]
    if options.verbose:
        print histPaths[h]
        
    if drawRules.drawratio is None:
        HISTPAD = CANVAS
    drawRules.draw(histPath)
    
