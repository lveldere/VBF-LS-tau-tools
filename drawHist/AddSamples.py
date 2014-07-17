import mytools,shutil
import glob, os, sys

from optparse import OptionParser

# parse command line arguments
parser = OptionParser()
parser.add_option("--idir",dest="idir",default="input",help="path to input directory with root files, default=%default")
(options, args) = parser.parse_args()

options.idir = options.idir.rstrip("/")

# check options
def checkLocationOption(location,title,option):
    if not os.path.exists(location):
        print "ERROR: given {0}, {1}, does not exist.".format(title,location)
        print "       Specify {0} with option {1}.".format(title,option)
        sys.exit()
	
print "INPUT DIR: " + options.idir
os.system("hadd -f "+options.idir+"/allDY.root "+options.idir+"/DY*.root")
os.system("hadd -f "+options.idir+"/allData.root "+options.idir+"/Tau*.root")
os.system("hadd -f "+options.idir+"/allHiggs.root "+options.idir+"/VBF*.root")
os.system("hadd -f "+options.idir+"/allQCD.root "+options.idir+"/QCD_Pt*.root")
os.system("hadd -f "+options.idir+"/allT.root "+options.idir+"/T*channel*.root")
os.system("hadd -f "+options.idir+"/allTTbar.root "+options.idir+"/TTJets.root")
os.system("hadd -f "+options.idir+"/allVV.root "+options.idir+"/WW*.root "+options.idir+"/WZ*.root "+options.idir+"/ZZ*.root "+options.idir+"/W*qq.root")
os.system("hadd -f "+options.idir+"/allW.root "+options.idir+"/W*ToLNu.root")

os.system("cp "+options.idir+"/allQCD.root "+options.idir+"/QCD_OS-SR.root")
os.system("cp "+options.idir+"/allQCD.root "+options.idir+"/QCD_OS-CR2.root")
os.system("cp "+options.idir+"/allQCD.root "+options.idir+"/QCD_OS-CR3.root")
os.system("cp "+options.idir+"/allQCD.root "+options.idir+"/QCD_OS-CR4.root")
os.system("cp "+options.idir+"/allQCD.root "+options.idir+"/QCD_OS-CR5.root")
os.system("cp "+options.idir+"/allQCD.root "+options.idir+"/QCD_OS-CR6.root")
os.system("cp "+options.idir+"/allQCD.root "+options.idir+"/QCD_OS-CR7.root")
os.system("cp "+options.idir+"/allQCD.root "+options.idir+"/QCD_OS-CR8.root")
os.system("cp "+options.idir+"/allQCD.root "+options.idir+"/QCD_OS-CR9.root")
os.system("cp "+options.idir+"/allQCD.root "+options.idir+"/QCD_OS-CR10.root")
os.system("cp "+options.idir+"/allQCD.root "+options.idir+"/QCD_LS-SR.root")
os.system("cp "+options.idir+"/allQCD.root "+options.idir+"/QCD_LS-CR2.root")
os.system("cp "+options.idir+"/allQCD.root "+options.idir+"/QCD_LS-CR3.root")
os.system("cp "+options.idir+"/allQCD.root "+options.idir+"/QCD_LS-CR4.root")
os.system("cp "+options.idir+"/allQCD.root "+options.idir+"/QCD_LS-CR5.root")
os.system("cp "+options.idir+"/allQCD.root "+options.idir+"/QCD_LS-CR6.root")
os.system("cp "+options.idir+"/allQCD.root "+options.idir+"/QCD_LS-CR7.root")
os.system("cp "+options.idir+"/allQCD.root "+options.idir+"/QCD_LS-CR8.root")
os.system("cp "+options.idir+"/allQCD.root "+options.idir+"/QCD_LS-CR9.root")
os.system("cp "+options.idir+"/allQCD.root "+options.idir+"/QCD_LS-CR10.root")
