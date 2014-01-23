{
#include <TROOT.h>
#include <TDirectory.h>
#include <TCanvas.h>
#include <TFile.h>
#include <TH1F.h>
#include <TH2F.h>
#include <TString.h>
#include <TGraphAsymmErrors.h>

cout << "Begin" << endl;

TCanvas* c= new TCanvas("c", "c",1);
c->cd();
c->Clear();

TGraphAsymmErrors g_triggereff_tau1pt_noIso((TH1F*)(_file0->Get("Skim_noIso_wiTrigger/h_tau1pt")),(TH1F*)(_file0->Get("Skim_noIso_woTrigger/h_tau1pt")));
g_triggereff_tau1pt_noIso->SetTitle("triggereff_vs_tau1pt_noIso");
g_triggereff_tau1pt_noIso->Draw("AP");
c->SaveAs("g_triggereff_tau1pt_noIso.png");
c->Clear();


TGraphAsymmErrors g_triggereff_tau1pt_looseIso((TH1F*)(_file0->Get("Skim_looseIso_wiTrigger/h_tau1pt")),(TH1F*)(_file0->Get("Skim_looseIso_woTrigger/h_tau1pt")));
g_triggereff_tau1pt_looseIso->SetTitle("triggereff_vs_tau1pt_looseIso");
g_triggereff_tau1pt_looseIso->Draw("AP");
c->SaveAs("g_triggereff_tau1pt_looseIso.png");
c->Clear();

TGraphAsymmErrors g_triggereff_tau1pt_mediumIso((TH1F*)(_file0->Get("Skim_mediumIso_wiTrigger/h_tau1pt")),(TH1F*)(_file0->Get("Skim_mediumIso_woTrigger/h_tau1pt")));
g_triggereff_tau1pt_mediumIso->SetTitle("triggereff_vs_tau1pt_mediumIso");
g_triggereff_tau1pt_mediumIso->Draw("AP");
c->SaveAs("g_triggereff_tau1pt_mediumIso.png");
c->Clear();

TGraphAsymmErrors g_triggereff_tau1pt_tightIso((TH1F*)(_file0->Get("Skim_tightIso_wiTrigger/h_tau1pt")),(TH1F*)(_file0->Get("Skim_tightIso_woTrigger/h_tau1pt")));
g_triggereff_tau1pt_tightIso->SetTitle("triggereff_vs_tau1pt_tightIso");
g_triggereff_tau1pt_tightIso->Draw("AP");
c->SaveAs("g_triggereff_tau1pt_tightIso.png");
c->Clear();

TGraphAsymmErrors g_triggereff_tau2pt_noIso((TH1F*)(_file0->Get("Skim_noIso_wiTrigger/h_tau2pt")),(TH1F*)(_file0->Get("Skim_noIso_woTrigger/h_tau2pt")));
g_triggereff_tau2pt_noIso->SetTitle("triggereff_vs_tau2pt_noIso");
g_triggereff_tau2pt_noIso->Draw("AP");
c->SaveAs("g_triggereff_tau2pt_noIso.png");
c->Clear();


TGraphAsymmErrors g_triggereff_tau2pt_looseIso((TH1F*)(_file0->Get("Skim_looseIso_wiTrigger/h_tau2pt")),(TH1F*)(_file0->Get("Skim_looseIso_woTrigger/h_tau2pt")));
g_triggereff_tau2pt_looseIso->SetTitle("triggereff_vs_tau2pt_looseIso");
g_triggereff_tau2pt_looseIso->Draw("AP");
c->SaveAs("g_triggereff_tau2pt_looseIso.png");
c->Clear();

TGraphAsymmErrors g_triggereff_tau2pt_mediumIso((TH1F*)(_file0->Get("Skim_mediumIso_wiTrigger/h_tau2pt")),(TH1F*)(_file0->Get("Skim_mediumIso_woTrigger/h_tau2pt")));
g_triggereff_tau2pt_mediumIso->SetTitle("triggereff_vs_tau2pt_mediumIso");
g_triggereff_tau2pt_mediumIso->Draw("AP");
c->SaveAs("g_triggereff_tau2pt_mediumIso.png");
c->Clear();

TGraphAsymmErrors g_triggereff_tau2pt_tightIso((TH1F*)(_file0->Get("Skim_tightIso_wiTrigger/h_tau2pt")),(TH1F*)(_file0->Get("Skim_tightIso_woTrigger/h_tau2pt")));
g_triggereff_tau2pt_tightIso->SetTitle("triggereff_vs_tau2pt_tightIso");
g_triggereff_tau2pt_tightIso->Draw("AP");
c->SaveAs("g_triggereff_tau2pt_tightIso.png");
c->Clear();

cout << "End" << endl;

}
