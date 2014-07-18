import mytools,shutil
import glob, os, sys

from optparse import OptionParser

# parse command line arguments
parser = OptionParser()
parser.add_option("--idir",dest="idir",default="input",help="path to input directory with root files, default=%default")
parser.add_option("--LS_SR",dest="LS_SR",default="0",help="expected QCD events in LS signal region default=%default")
parser.add_option("--OS_SR",dest="OS_SR",default="0",help="expected QCD events in OS signal region default=%default")
parser.add_option("--Lumi",dest="Lumi",default="19712",help="Overall luminosity used default=%default")
(options, args) = parser.parse_args()

options.idir = options.idir.rstrip("/")

print "INPUT DIR: " + options.idir

print "Recalculating errors according to efficiency"
os.system("root -b -q 'EfficiencyErrorCalc.C++g(\""+options.idir+"\")'")

print "Weighting samples to cross section and luminosity"
os.system("./weightHist.py --idir "+options.idir)

print "Adding histograms by background/data/signal-type"
os.system("python AddSamples.py --idir "+options.idir+"_weighted")

print "Determining and writing QCD scale factor .txt-file"
os.system("root -l -b -q 'SFcalculator.C(\""+options.idir+"_weighted\", "+options.Lumi+", "+options.LS_SR+", "+options.OS_SR+")'&>RawScaleFactors_"+options.idir+".txt")
lines = open("RawScaleFactors_"+options.idir+".txt").readlines()
open("ScaleFactors_"+options.idir+".txt", 'w').writelines(lines[2:])
os.system("rm RawScaleFactors_"+options.idir+".txt")

print "Scaling and drawing nice plots"
os.system("python DrawScaledDistributions.py --idir "+options.idir)
