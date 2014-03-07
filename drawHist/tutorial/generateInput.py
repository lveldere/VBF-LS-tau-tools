#!/usr/bin/env python

import sys,os

# import root in batch mode
sys.argv.append("-b")
import ROOT as rt

###############################################
# generate input files for a drawHist tutorial
###############################################

# bkg1: 
#    - p(var1|bkg1) = expo(-var1/200)
#    - p(var2|bkg1) = expo(-var2/20)
# bkg2: gaussian shape in var1,
#    - p(var1|bkg2) = gaus(var1;200,100)
#    - p(var2|bkg2) = expo(var2/50)
# signal, component 1
#    - p(var1|sig1) = gaus(var1;400,75)
#    - p(var2|sig1) = gaus(var2;50,25)
# signal component 2
#    - p(var1|sig2) = gauss(var1;430,20)
#    - p(var1|sig2) = gauss(var2;60,10)

#####################
# BEGIN OPTIONS
#####################

var = [
    {"name":"var1","nbin":100,"min":0,"max":600},
    {"name":"var2","nbin":100,"min":0,"max":100}
]

str_gaus = "1./([1]*TMath::Sqrt(2*TMath::Pi()))*TMath::Exp(-TMath::Power((x-[0])/[1],2)/2)"
str_expo = "[0]*TMath::Exp(-x*[0])"

species = [
    {
        "name":"bkg1",
        "var1":{"pdf":str_expo,"parameters":[1./200]},
        "var2":{"pdf":str_expo,"parameters":[1./20]},
        "file":"bkg1.root",
        "N":10000
        },
    {
        "name":"bkg2",
        "var1":{"pdf":str_gaus,"parameters":[200,100]},
        "var2":{"pdf":str_expo,"parameters":[1./50]},
        "file":"bkg2.root",
        "N":10000
        },
    {
        "name":"sig1",
        "var1":{"pdf":str_gaus,"parameters":[400,75]},
        "var2":{"pdf":str_gaus,"parameters":[50,25]},
        "file":"sig.root:component1",
        "N":3000
        },
    {
        "name":"sig2",
        "var1":{"pdf":str_gaus,"parameters":[430,20]},
        "var2":{"pdf":str_gaus,"parameters":[60,10]},
        "file":"sig.root:component2",
        "N":7000
        }
    ]

#####################
# END OPTIONS
#####################

#####################
# creat output root files
#####################
dict_tfile = dict()
dict_counts = dict()
dict_tdir = dict()
dict_hist = dict()
for _species in species:
    _list = _species["file"].split(":")
    # create output root file
    path_tfile = _list[0]
    if not path_tfile in dict_tfile:
        dict_tfile[path_tfile] = rt.TFile.Open("input/" + path_tfile,"RECREATE")
        _hist = rt.TH1D("counts","counts",1,0,1)
        _hist.Fill(0,_species["N"])
        dict_counts[path_tfile] = _hist
    else:
        dict_counts[path_tfile].Fill(0,_species["N"])
    # create output directory
    _tdir = dict_tfile[path_tfile]
    if len(_list) == 2:
        path_tdir = _list[1].lstrip("/")
        _tdir = dict_tfile[path_tfile].mkdir(path_tdir)
    dict_tdir[_species["name"]] = _tdir
    dict_hist[_species["name"]] = []
    

#####################
# generate histograms
#####################
for _species in species:
    dict_tdir[_species["name"]].cd()
    # the variables
    for _var in var:
        _varname = _var["name"]
        _hist = rt.TH1D(_var["name"],_var["name"],_var["nbin"],_var["min"],_var["max"])
        pdfname = _species["name"] + "_" + _var["name"]
        pdf = rt.TF1(pdfname,_species[_varname]["pdf"],_var["min"],_var["max"])
        parameters = _species[_varname]["parameters"]
        for p in range(0,len(parameters)):
            pdf.SetParameter(p,parameters[p])
        _hist.FillRandom(pdfname,_species["N"])
        dict_hist[_species["name"]].append(_hist)
   
#####################
# write histograms
#####################
for key in dict_counts:
    dict_tfile[key].cd()
    dict_counts[key].Write()
for _species in species:
    dict_tdir[_species["name"]].cd()
    for _hist in dict_hist[_species["name"]]:
        _hist.Write()
#####################
# and close files
#####################
for tfile in dict_tfile.values():
    tfile.Close()






