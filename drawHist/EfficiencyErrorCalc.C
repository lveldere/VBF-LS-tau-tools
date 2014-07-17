#include "TROOT.h"
#include "TFile.h"
#include "TProfile.h"
#include "TH1F.h"
#include "TMath.h"
#include "TString.h"
#include <iostream>

void RecalculateErrors(TH1F* hist, TProfile *profile)
{
  for(int i=0; i<hist->GetNbinsX(); i++){
    double eff=profile->GetBinContent(i+1);
    double N  =profile->GetBinEntries(i+1);
    //std::cout<<"bin "<<i<<": before="<<hist->GetBinError(i+1);
    if(N>0) hist->SetBinError(i+1, TMath::Sqrt(eff*(1-eff)/N));
    else hist->SetBinError(i+1, 0);
    //std::cout<<", after="<<hist->GetBinError(i+1)<<std::endl;
  }
}

void WriteNewHists(TFile *input, TString directory, TString histname)
{
  TString dest ="h_";
  dest.Append(histname);
  TString pdest="p_";
  pdest.Append(histname);
  std::cout<<"changing histogram "<<dest<<" with profile "<<pdest<<std::endl;
  dest.Prepend(directory);
  pdest.Prepend(directory);
  pdest.Prepend("p_");
  TH1F* hist=(TH1F*)input->Get(dest);
  RecalculateErrors((TH1F*)hist,(TProfile*)input->Get(pdest));
  hist->Write();
}

vector<TString> Histnames(vector<TString> list)
{
  list.push_back("njet");
  list.push_back("jetpt");
  list.push_back("jeteta");
  list.push_back("jet1pt");
  list.push_back("jet1eta");
  list.push_back("jet2pt");
  list.push_back("jet2eta");
  list.push_back("dijetinvariantmass");
  list.push_back("dijetdeltaeta");
  list.push_back("tau1pt");
  list.push_back("tau1eta");
  list.push_back("tau2pt");
  list.push_back("tau2eta");
  list.push_back("ditauinvariantmass");
  list.push_back("ditaucharge");
  list.push_back("ditaucosdeltaphi");
  list.push_back("ditaudeltaeta");
  list.push_back("met");
  list.push_back("ht");
  list.push_back("ht_withtau");
  return list;
}

vector<TString> Filenames(vector<TString> list, TString origin)
{
  list.push_back("/DYToEE.root");
  list.push_back("/DYToMuMu.root");
  list.push_back("/DYToTauTau.root");
  list.push_back("/QCD_Pt-30to50.root");
  list.push_back("/QCD_Pt-50to80.root");
  list.push_back("/QCD_Pt-80to120.root");
  list.push_back("/QCD_Pt-120to170.root");
  list.push_back("/QCD_Pt-170to300.root");
  list.push_back("/QCD_Pt-300to470.root");
  list.push_back("/QCD_Pt-470to600.root");
  list.push_back("/QCD_Pt-600to800.root");
  list.push_back("/QCD_Pt-800to1000.root");
  list.push_back("/QCD_Pt-1000to1400.root");
  list.push_back("/QCD_Pt-1400to1800.root");
  list.push_back("/QCD_Pt-1800.root");
  list.push_back("/TTJets.root");
  list.push_back("/T_s-channel.root");
  list.push_back("/T_t-channel.root");
  list.push_back("/T_tW-channel-DR.root");
  list.push_back("/Tbar_s-channel.root");
  list.push_back("/Tbar_t-channel.root");
  list.push_back("/Tbar_tW-channel-DR.root");
  list.push_back("/VBFToHToZZTo2L2Nu_M-124.root");
  list.push_back("/VBF_HToTauTau_M-125.root");
  list.push_back("/VBF_HToWWTo2LAndTau2Nu_M-125.root");
  list.push_back("/VBF_HToZZTo2L2Q_M-125.root");
  list.push_back("/VBF_HToZZTo4Nu_M-125.root");
  list.push_back("/WJetsToLNu.root");
  list.push_back("/W1JetsToLNu.root");
  list.push_back("/W2JetsToLNu.root");
  list.push_back("/W3JetsToLNu.root");
  list.push_back("/W4JetsToLNu.root");
  list.push_back("/WW.root");
  list.push_back("/WW_DoubleScattering.root");
  list.push_back("/WmWmqq.root");
  list.push_back("/WpWpqq.root");
  list.push_back("/WZJetsTo2L2Q.root");
  list.push_back("/WZJetsTo2Q2Nu.root");
  list.push_back("/WZJetsTo3LNu.root");
  list.push_back("/ZZJetsTo2L2Nu.root");
  list.push_back("/ZZJetsTo2L2Q.root");
  list.push_back("/ZZJetsTo2Q2Nu.root");
  list.push_back("/ZZJetsTo4L.root");
  for(unsigned int l=0; l<list.size(); l++) list[l].Prepend(origin);
  return list;
}

vector<TString> Directorynames(vector<TString> list)
{
  list.push_back("LS_SignalRegion/");
  list.push_back("LS_Central_invertedVBF_2TightIso_CR2/");
  list.push_back("LS_SignalRegion_M0/");
  list.push_back("LS_Central_invertedVBF_2TightIso_CR2_M0/");  
  list.push_back("LS_Central_1TightIso_CR3/");
  list.push_back("LS_Central_invertedVBF_1TightIso_CR4/");
  list.push_back("LS_Central_AntiTightIso_CR5/");
  list.push_back("LS_Central_invertedVBF_AntiTightIso_CR6/");  
  list.push_back("LS_Central_AntiMediumIso_CR7/");
  list.push_back("LS_Central_invertedVBF_AntiMediumIso_CR8/");  
  list.push_back("OS_SignalRegion/");
  list.push_back("OS_Central_invertedVBF_2TightIso_CR2/");
  list.push_back("OS_SignalRegion_M0/");
  list.push_back("OS_Central_invertedVBF_2TightIso_CR2_M0/");  
  list.push_back("OS_Central_1TightIso_CR3/");
  list.push_back("OS_Central_invertedVBF_1TightIso_CR4/");
  list.push_back("OS_Central_AntiTightIso_CR5/");
  list.push_back("OS_Central_invertedVBF_AntiTightIso_CR6/");  
  list.push_back("OS_Central_AntiMediumIso_CR7/");
  list.push_back("OS_Central_invertedVBF_AntiMediumIso_CR8/");   
  return list;
}

void EfficiencyErrorCalc(TString origin)
{
  vector<TString> hists, files, directories;
  hists=Histnames(hists);
  files=Filenames(files, origin);
  directories=Directorynames(directories);
  std::cout<<"N_files: "<<files.size()<<", N_directories: "<<directories.size()<<", N_hists"<<hists.size()<<std::endl;
  for(unsigned int f=0; f<files.size(); f++)
    {
      for(unsigned int d=0; d<directories.size(); d++)
        {
	  for(unsigned int h=0; h<hists.size(); h++)
   	   {
      	 	std::cout<<"f: "<<f<<", d: "<<d<<", h: "<<h<<std::endl;
      		TFile *file=(TFile*)TFile::Open((TString)files[f],"UPDATE");
      		WriteNewHists((TFile*)file, directories[d], hists[h]);
      		file->Close();
	   }
	}
    }
}
