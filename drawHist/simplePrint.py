#!/usr/bin/env python

import sys,tempfile,os,shutil

ifile = sys.argv[1]
odir = sys.argv[2]

# the input directory
idir = tempfile.mkdtemp(dir="./",suffix="_idir")
shutil.rmtree(idir)
os.mkdir(idir)
shutil.copyfile(ifile,idir + "/" + os.path.split(ifile)[1])

# the histRule file
histRules = tempfile.mkstemp(dir="./",suffix="_histRules.cfg")
histRules_str=("""
[main]
draw=file
drawlegend=0

[Hist file]
files=__TEMP__
""")
histRules_str = histRules_str.replace("__TEMP__",os.path.split(ifile)[1].replace(".root",""))
FILE = open(histRules[1],"w")
FILE.write(histRules_str)
FILE.close()

# the drawHist command
c = "./drawHist.py --drawrules=" + histRules[1] + " --idir=" + idir + " --force" + " --odir " + odir
os.system(c)

# cleanup
os.remove(histRules[1])
shutil.rmtree(idir)
