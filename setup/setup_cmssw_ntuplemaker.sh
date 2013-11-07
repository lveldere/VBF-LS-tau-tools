echo "Please input your CERN username: "
read input_variable

ini -d cmssw
ini cmssw_cvmfs 
kinit $input_variable@CERN.CH

scram project CMSSW CMSSW_5_3_11_patch6

cd CMSSW_5_3_11_patch6/src/
cmsenv

git cms-addpkg PhysicsTools/PatAlgos
git cms-merge-topic vadler:53X-addMVAElectronId
git cms-addpkg PhysicsTools/PatUtils
git cms-merge-topic -u vadler:53X-tagset133511-newBTagging
git cms-merge-topic -u vadler:53X-tagset133511-newEGIsolation
git cms-merge-topic -u cms-tau-pog:CMSSW_5_3_X_HighPt
cvs co -d SHarper/HEEPAnalyzer -r V00-09-03 UserCode/SHarper/HEEPAnalyzer
cvs co -d CMGTools/External -r V00-03-04 UserCode/CMG/CMGTools/External
git cms-merge-topic -u TaiSakuma:53X-met-130910-01
cvs co -d HighMassAnalysis/Configuration -r for537_02182013 UserCode/AlfredoGurrola/HighMassAnalysis/Configuration
cvs co -d HighMassAnalysis/Skimming -r for537_02182013 UserCode/AlfredoGurrola/HighMassAnalysis/Skimming
cp /afs/naf.desy.de/user/m/marconi/public/VBFPATupleProducer/hiMassTau_patProd.py $CMSSW_BASE/src/HighMassAnalysis/Configuration/test/Data_TauTauSkim/hiMassTau_patProd.py
cp /afs/naf.desy.de/user/m/marconi/public/VBFPATupleProducer/patTupleEventContentForHiMassTau_cff.py $CMSSW_BASE/src/HighMassAnalysis/Configuration/python/patTupleEventContentForHiMassTau_cff.py

cd $CMSSW_BASE/src/JetMETCorrections/Type1MET/python/
rm -v pfMETsysShiftCorrections_cfi.py
wget http://dl.dropbox.com/u/206488/CMS/RA2TAU/VBF-re-PATTuples/pfMETsysShiftCorrections_cfi.py
scram b clean
scram build -c
scram b -j 8

cd $CMSSW_BASE/src/PhysicsTools
git clone https://github.com/hbprosper/TheNtupleMaker.git
cd TheNtupleMaker
cmsenv
scripts/initTNM.py

scram b clean
scram b -j 8
