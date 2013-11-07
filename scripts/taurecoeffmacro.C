{
#include <TROOT.h>
#include <TDirectory.h>
#include <TCanvas.h>
#include <TFile.h>
#include <TH1F.h>
#include <TH2F.h>


cout<<"begin"<<endl;

//TFile _file0 ("VBFSUSY_C1pmC1pm_8TeV.root","UPDATE");
TFile _file0 ("VBFSUSY_C1pmC1pm_test.root","UPDATE");

((TH1F*)(_file0->Get("h_matchTightIsoGenPt")))->Clone("h_matchTightIsoGenPt_eff");

((TH1F*)(_file0->Get("h_matchTightIsoGenPt_eff")))->Divide((TH1F*)(_file0->Get("h_gentaupt")));

((TH1F*)(_file0->Get("h_matchTightIsoGenPt_eff")))->Write();

((TH1F*)(_file0->Get("h_matchMediumIsoGenPt")))->Clone("h_matchMediumIsoGenPt_eff");

((TH1F*)(_file0->Get("h_matchMediumIsoGenPt_eff")))->Divide((TH1F*)(_file0->Get("h_gentaupt")));

((TH1F*)(_file0->Get("h_matchMediumIsoGenPt_eff")))->Write();

((TH1F*)(_file0->Get("h_matchLooseIsoGenPt")))->Clone("h_matchLooseIsoGenPt_eff");

((TH1F*)(_file0->Get("h_matchLooseIsoGenPt_eff")))->Divide((TH1F*)(_file0->Get("h_gentaupt")));

((TH1F*)(_file0->Get("h_matchLooseIsoGenPt_eff")))->Write();

cout<<"end"<<endl;

}
