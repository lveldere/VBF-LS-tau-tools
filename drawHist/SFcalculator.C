#include "TROOT.h"
#include "TFile.h"
#include "TMath.h"
#include "TH1F.h"
#include <iostream>
#include "TF1.h"
#include "TCanvas.h"
#include "TString.h"

vector<TString> Filenames(vector<TString> list, TString origin)
{
  list.push_back("/allData.root");	//has to be the first file
  list.push_back("/allQCD.root");	//has to be the second file
  list.push_back("/allDY.root");	//has to be the first file  
  list.push_back("/allHiggs.root");
  list.push_back("/allT.root");
  list.push_back("/allTTbar.root");
  list.push_back("/allVV.root");
  list.push_back("/allW.root");
  for(unsigned int l=0; l<list.size(); l++) list[l].Prepend(origin);
  return list;
}

vector<TString> Directorynames(vector<TString> list)
{
  list.push_back("LS_SignalRegion/");
  list.push_back("LS_Central_invertedVBF_2TightIso_CR2/");  
  list.push_back("LS_Central_1TightIso_CR3/");
  list.push_back("LS_Central_invertedVBF_1TightIso_CR4/");
  list.push_back("LS_Central_AntiTightIso_CR5/");
  list.push_back("LS_Central_invertedVBF_AntiTightIso_CR6/");  
  list.push_back("LS_Central_AntiMediumIso_CR7/");
  list.push_back("LS_Central_invertedVBF_AntiMediumIso_CR8/"); 
  list.push_back("LS_Central_AntiLooseIso_CR9/");
  list.push_back("LS_Central_invertedVBF_AntiLooseIso_CR10/");   
  list.push_back("OS_SignalRegion/");
  list.push_back("OS_Central_invertedVBF_2TightIso_CR2/"); 
  list.push_back("OS_Central_1TightIso_CR3/");
  list.push_back("OS_Central_invertedVBF_1TightIso_CR4/");
  list.push_back("OS_Central_AntiTightIso_CR5/");
  list.push_back("OS_Central_invertedVBF_AntiTightIso_CR6/");  
  list.push_back("OS_Central_AntiMediumIso_CR7/");
  list.push_back("OS_Central_invertedVBF_AntiMediumIso_CR8/");  
  list.push_back("OS_Central_AntiLooseIso_CR9/");
  list.push_back("OS_Central_invertedVBF_AntiLooseIso_CR10/");   
  return list;
}

void SFcalculator(TString origin, double Lumi, double LS_SR, double OS_SR){

  bool verbose = false;

  vector<TString> files, directories;
  files=Filenames(files, origin);
  directories=Directorynames(directories);
  vector<double> events;
  vector<double> QCD;
  double AllEvents=0.;
  //initialize vectors
  for(unsigned int d=0; d<directories.size(); d++){
    events.push_back(0.);
    QCD.push_back(0.);
  }
  for(unsigned int f=0; f<files.size(); f++)
    {
      double sign=0.;
      if(f==0) sign=+1.;
      else if(f==1){
        TFile* file=(TFile*)TFile::Open((TString)files[f],"READ");
	TH1F*count=(TH1F*)file->Get("counts");
	AllEvents=count->Integral();
	file->Close();
      }
      else if(f>1) sign=-1.;
      for(unsigned int d=0; d<directories.size(); d++)
        {
	  TFile* file=(TFile*)TFile::Open((TString)files[f],"READ");
	  TString dest="h_ditaucharge";
	  dest.Prepend(directories[d]);
	  if(verbose)cout<<"f: "<<f<<", d: "<<d<<" in "<<files[f]<<" at "<<dest<<endl;
	  TH1F* count=(TH1F*)file->Get(dest);
          events[d]+=sign*count->Integral();
	  if(sign==0)QCD[d]=count->Integral();
	  file->Close();
	}
    }
  if(Lumi<=0) return;
  //print scaling factors table
  cout<<"# QCD scaling factors"<<endl;
  if(QCD[0]>0) cout<<"QCD_LS-SR   1 "<<LS_SR/QCD[0]/Lumi*AllEvents<<endl;
  if(QCD[1]>0) cout<<"QCD_LS-CR2  1 "<<events[1]/QCD[1]/Lumi*AllEvents<<endl;
  if(QCD[2]>0) cout<<"QCD_LS-CR3  1 "<<events[2]/QCD[2]/Lumi*AllEvents<<endl;
  if(QCD[3]>0) cout<<"QCD_LS-CR4  1 "<<events[3]/QCD[3]/Lumi*AllEvents<<endl;
  if(QCD[4]>0) cout<<"QCD_LS-CR5  1 "<<events[4]/QCD[4]/Lumi*AllEvents<<endl;
  if(QCD[5]>0) cout<<"QCD_LS-CR6  1 "<<events[5]/QCD[5]/Lumi*AllEvents<<endl;
  if(QCD[6]>0) cout<<"QCD_LS-CR7  1 "<<events[6]/QCD[6]/Lumi*AllEvents<<endl;
  if(QCD[7]>0) cout<<"QCD_LS-CR8  1 "<<events[7]/QCD[7]/Lumi*AllEvents<<endl;  
  if(QCD[8]>0) cout<<"QCD_LS-CR9  1 "<<events[8]/QCD[8]/Lumi*AllEvents<<endl;
  if(QCD[9]>0) cout<<"QCD_LS-CR10 1 "<<events[9]/QCD[9]/Lumi*AllEvents<<endl;  
  if(QCD[10]>0) cout<<"QCD_OS-SR   1 "<<OS_SR/QCD[10]/Lumi*AllEvents<<endl;
  if(QCD[11]>0) cout<<"QCD_OS-CR2  1 "<<events[11]/QCD[11]/Lumi*AllEvents<<endl;
  if(QCD[12]>0) cout<<"QCD_OS-CR3  1 "<<events[12]/QCD[12]/Lumi*AllEvents<<endl;
  if(QCD[13]>0) cout<<"QCD_OS-CR4  1 "<<events[13]/QCD[13]/Lumi*AllEvents<<endl;
  if(QCD[14]>0) cout<<"QCD_OS-CR5  1 "<<events[14]/QCD[14]/Lumi*AllEvents<<endl;
  if(QCD[15]>0) cout<<"QCD_OS-CR6  1 "<<events[15]/QCD[15]/Lumi*AllEvents<<endl;
  if(QCD[16]>0) cout<<"QCD_OS-CR7  1 "<<events[16]/QCD[16]/Lumi*AllEvents<<endl;
  if(QCD[17]>0) cout<<"QCD_OS-CR8  1 "<<events[17]/QCD[17]/Lumi*AllEvents<<endl;  
  if(QCD[18]>0) cout<<"QCD_OS-CR9  1 "<<events[18]/QCD[18]/Lumi*AllEvents<<endl;
  if(QCD[19]>0) cout<<"QCD_OS-CR10 1 "<<events[19]/QCD[19]/Lumi*AllEvents<<endl;         
}
