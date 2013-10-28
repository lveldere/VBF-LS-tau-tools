cmsenv

addpkg DataFormats/PatCandidates V06-05-06-05
addpkg PhysicsTools/PatAlgos     V08-09-51
addpkg DataFormats/StdDictionaries V00-02-14
addpkg FWCore/GuiBrowsers V00-00-70
addpkg RecoParticleFlow/PFProducer V15-02-06
addpkg RecoTauTag/RecoTau V01-04-23
addpkg RecoTauTag/Configuration V01-04-10
addpkg CondFormats/EgammaObjects V00-04-00
addpkg JetMETCorrections/Type1MET V04-06-09
addpkg PhysicsTools/PatUtils V03-09-23
addpkg CommonTools/ParticleFlow V00-03-16                              
addpkg CommonTools/RecoAlgos V00-03-23      
addpkg CommonTools/RecoUtils V00-00-13  
addpkg DataFormats/ParticleFlowCandidate V15-03-03
addpkg DataFormats/TrackReco V10-02-02      
addpkg DataFormats/VertexReco V02-00-04      
cvs co -d SHarper/HEEPAnalyzer UserCode/SHarper/HEEPAnalyzer
cvs co -d HighMassAnalysis/Skimming -r for537_02182013 UserCode/AlfredoGurrola/HighMassAnalysis/Skimming
cvs co -d HighMassAnalysis/Configuration -r for537_02182013 UserCode/AlfredoGurrola/HighMassAnalysis/Configuration
cvs co -d HighMassAnalysis/Analysis -r forVBFSusy_07222012 UserCode/AlfredoGurrola/HighMassAnalysis/Analysis
scram b -j 8

cd PhysicsTools
cvs co -r v5_4_1 -d TheNtupleMaker UserCode/SusySapien/PhysicsTools/TheNtupleMaker
cd TheNtupleMaker
scripts/initTNM.py
scram b clean
scram b -j 8

cd $CMSSW_BASE
mkdir $CMSSW_BASE/src/ntuples    # add ntuple package
git clone https://github.com/rathjd/VBF-LS-tau-ntupler $CMSSW_BASE/src/ntuples/VBF-LS-tau-ntupler
scram b -j 8
