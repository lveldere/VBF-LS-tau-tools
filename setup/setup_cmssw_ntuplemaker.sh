echo "Please input your CERN username: "
read input_variable

ini -d cmssw
ini cmssw_cvmfs
kinit $input_variable@CERN.CH

scram project CMSSW CMSSW_5_3_11_patch6

cd CMSSW_5_3_11_patch6/src/
cmsenv

git cms-addpkg CondFormats/JetMETObjects
git cms-addpkg PhysicsTools/PatAlgos
git cms-addpkg PhysicsTools/PatUtils
git cms-merge-topic -u cms-tau-pog:CMSSW_5_3_X_boostedTaus_2013Dec17
git cms-merge-topic -u TaiSakuma:53X-met-130910-01
cd $CMSSW_BASE/src/
git clone https://github.com/Sam-Harper/usercode SHarper
cd SHarper
git checkout V00-09-03
cd $CMSSW_BASE/src/
mkdir CMGTools
cd CMGTools
git clone https://github.com/h2gglobe/External External
cd ../
cd $CMSSW_BASE/src/
git clone https://github.com/CMSRA2Tau/HighMassAnalysis HighMassAnalysis
cd $CMSSW_BASE/src/JetMETCorrections/Type1MET/python/
rm -v pfMETsysShiftCorrections_cfi.py
wget --no-check-certificate http://dl.dropbox.com/u/206488/CMS/RA2TAU/VBF-re-PATTuples/pfMETsysShiftCorrections_cfi.py
scram b clean
scram build -c
scram b -j 8

cd $CMSSW_BASE/src/PhysicsTools
git clone https://github.com/hbprosper/TheNtupleMaker.git
cd TheNtupleMaker
cmsenv
scripts/initTNM.py

cd $CMSSW_BASE/src/
mkdir ntuples
cd ntuples
git clone https://github.com/rathjd/VBF-LS-tau-ntupler

cd $CMSSW_BASE/src/

scram b clean
scram b -j 8
