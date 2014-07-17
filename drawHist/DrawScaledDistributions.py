import mytools,shutil
import glob, os, sys

from optparse import OptionParser

# parse command line arguments
parser = OptionParser()
parser.add_option("--idir",dest="idir",default="input",help="path to input directory with root files, default=%default")
(options, args) = parser.parse_args()

options.idir = options.idir.rstrip("/")

os.system("./weightHist.py --idir "+options.idir+"_weighted --odir "+options.idir+"_scaled --xsecfile ScaleFactors_"+options.idir+".txt")
os.system("mkdir "+options.idir+"_scaled_output")
os.system("cp /nfs/dust/cms/user/rathjd/VBF-LS-tau/workdir/drawHist/NoMetNNI_scaled/*.cfg "+options.idir+"_scaled/.")
os.system("./drawHist.py --idir "+options.idir+"_scaled --odir "+options.idir+"_scaled_output/LS_SR --histpath='LS_SignalRegion' --drawrules "+options.idir+"_scaled/drawRules_LS_SR.cfg")
os.system("./drawHist.py --idir "+options.idir+"_scaled --odir "+options.idir+"_scaled_output/LS_CR2 --histpath='LS_Central_invertedVBF_2TightIso_CR2' --drawrules "+options.idir+"_scaled/drawRules_LS_CR2.cfg")
os.system("./drawHist.py --idir "+options.idir+"_scaled --odir "+options.idir+"_scaled_output/LS_CR3 --histpath='LS_Central_1TightIso_CR3' --drawrules "+options.idir+"_scaled/drawRules_LS_CR3.cfg")
os.system("./drawHist.py --idir "+options.idir+"_scaled --odir "+options.idir+"_scaled_output/LS_CR4 --histpath='LS_Central_invertedVBF_1TightIso_CR4' --drawrules "+options.idir+"_scaled/drawRules_LS_CR4.cfg")
os.system("./drawHist.py --idir "+options.idir+"_scaled --odir "+options.idir+"_scaled_output/LS_CR5 --histpath='LS_Central_AntiTightIso_CR5' --drawrules "+options.idir+"_scaled/drawRules_LS_CR5.cfg")
os.system("./drawHist.py --idir "+options.idir+"_scaled --odir "+options.idir+"_scaled_output/LS_CR6 --histpath='LS_Central_invertedVBF_AntiTightIso_CR6' --drawrules "+options.idir+"_scaled/drawRules_LS_CR6.cfg")
os.system("./drawHist.py --idir "+options.idir+"_scaled --odir "+options.idir+"_scaled_output/LS_CR7 --histpath='LS_Central_AntiMediumIso_CR7' --drawrules "+options.idir+"_scaled/drawRules_LS_CR7.cfg")
os.system("./drawHist.py --idir "+options.idir+"_scaled --odir "+options.idir+"_scaled_output/LS_CR8 --histpath='LS_Central_invertedVBF_AntiMediumIso_CR8' --drawrules "+options.idir+"_scaled/drawRules_LS_CR8.cfg")
os.system("./drawHist.py --idir "+options.idir+"_scaled --odir "+options.idir+"_scaled_output/LS_CR9 --histpath='LS_Central_AntiLooseIso_CR9' --drawrules "+options.idir+"_scaled/drawRules_LS_CR9.cfg")
os.system("./drawHist.py --idir "+options.idir+"_scaled --odir "+options.idir+"_scaled_output/LS_CR10 --histpath='LS_Central_invertedVBF_AntiLooseIso_CR10' --drawrules "+options.idir+"_scaled/drawRules_LS_CR10.cfg")
os.system("./drawHist.py --idir "+options.idir+"_scaled --odir "+options.idir+"_scaled_output/OS_SR --histpath='OS_SignalRegion' --drawrules "+options.idir+"_scaled/drawRules_OS_SR.cfg")
os.system("./drawHist.py --idir "+options.idir+"_scaled --odir "+options.idir+"_scaled_output/OS_CR2 --histpath='OS_Central_invertedVBF_2TightIso_CR2' --drawrules "+options.idir+"_scaled/drawRules_OS_CR2.cfg")
os.system("./drawHist.py --idir "+options.idir+"_scaled --odir "+options.idir+"_scaled_output/OS_CR3 --histpath='OS_Central_1TightIso_CR3' --drawrules "+options.idir+"_scaled/drawRules_OS_CR3.cfg")
os.system("./drawHist.py --idir "+options.idir+"_scaled --odir "+options.idir+"_scaled_output/OS_CR4 --histpath='OS_Central_invertedVBF_1TightIso_CR4' --drawrules "+options.idir+"_scaled/drawRules_OS_CR4.cfg")
os.system("./drawHist.py --idir "+options.idir+"_scaled --odir "+options.idir+"_scaled_output/OS_CR5 --histpath='OS_Central_AntiTightIso_CR5' --drawrules "+options.idir+"_scaled/drawRules_OS_CR5.cfg")
os.system("./drawHist.py --idir "+options.idir+"_scaled --odir "+options.idir+"_scaled_output/OS_CR6 --histpath='OS_Central_invertedVBF_AntiTightIso_CR6' --drawrules "+options.idir+"_scaled/drawRules_OS_CR6.cfg")
os.system("./drawHist.py --idir "+options.idir+"_scaled --odir "+options.idir+"_scaled_output/OS_CR7 --histpath='OS_Central_AntiMediumIso_CR7' --drawrules "+options.idir+"_scaled/drawRules_OS_CR7.cfg")
os.system("./drawHist.py --idir "+options.idir+"_scaled --odir "+options.idir+"_scaled_output/OS_CR8 --histpath='OS_Central_invertedVBF_AntiMediumIso_CR8' --drawrules "+options.idir+"_scaled/drawRules_OS_CR8.cfg")
os.system("./drawHist.py --idir "+options.idir+"_scaled --odir "+options.idir+"_scaled_output/OS_CR9 --histpath='OS_Central_AntiLooseIso_CR9' --drawrules "+options.idir+"_scaled/drawRules_OS_CR9.cfg")
os.system("./drawHist.py --idir "+options.idir+"_scaled --odir "+options.idir+"_scaled_output/OS_CR10 --histpath='OS_Central_invertedVBF_AntiLooseIso_CR10' --drawrules "+options.idir+"_scaled/drawRules_OS_CR10.cfg")
