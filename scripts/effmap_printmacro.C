{
#include <TROOT.h>
#include <TDirectory.h>
#include <TCanvas.h>
#include <TFile.h>
#include <TH1F.h>
#include <TH2F.h>
#include <TString.h>

cout<<"begin"<<endl;

//TFile _file0 ("analyzer_effmap_histograms.root","UPDATE");

TCanvas* c= new TCanvas("c", "c",1);
c->cd();

c->Clear();
((TH1F*)(_file0->Get("h1_jetpt")))->Draw();
c->SetLogy();
c->SaveAs("jetpt.png");

c->Clear();
((TH1F*)(_file0->Get("h1_jet1pt")))->Draw();
c->SetLogy();
c->SaveAs("jet1pt.png");
 
c->Clear();
((TH1F*)(_file0->Get("h1_jet2pt")))->Draw();
c->SetLogy();
c->SaveAs("jet2pt.png");

c->Clear();
((TH1F*)(_file0->Get("h1_taufakerate_pt_num")))->Clone("h1_taufakerate_pt_eff");
((TH1F*)(_file0->Get("h1_taufakerate_pt_eff")))->Divide((TH1F*)(_file0->Get("h1_taufakerate_pt_den")));
((TH1F*)(_file0->Get("h1_taufakerate_pt_eff")))->Draw();
((TH1F*)(_file0->Get("h1_taufakerate_pt_eff")))->GetXaxis()->SetRange(0,5);
c->SaveAs("taufakerate_pt_eff.png");

((TH1F*)(_file0->Get("h1_taufakerate_ptjet1_num")))->Clone("h1_taufakerate_ptjet1_eff");
((TH1F*)(_file0->Get("h1_taufakerate_ptjet1_eff")))->Divide((TH1F*)(_file0->Get("h1_taufakerate_ptjet1_den")));
((TH1F*)(_file0->Get("h1_taufakerate_ptjet1_eff")))->Draw();
((TH1F*)(_file0->Get("h1_taufakerate_ptjet1_eff")))->GetXaxis()->SetRange(0,5);
c->SaveAs("taufakerate_ptjet1_eff.png");

((TH1F*)(_file0->Get("h1_taufakerate_ptjet2_num")))->Clone("h1_taufakerate_ptjet2_eff");
((TH1F*)(_file0->Get("h1_taufakerate_ptjet2_eff")))->Divide((TH1F*)(_file0->Get("h1_taufakerate_ptjet2_den")));
((TH1F*)(_file0->Get("h1_taufakerate_ptjet2_eff")))->Draw();
((TH1F*)(_file0->Get("h1_taufakerate_ptjet2_eff")))->GetXaxis()->SetRange(0,5);
c->SaveAs("taufakerate_ptjet2_eff.png");

((TH1F*)(_file0->Get("h1_taufakerate_ptjet3_num")))->Clone("h1_taufakerate_ptjet3_eff");
((TH1F*)(_file0->Get("h1_taufakerate_ptjet3_eff")))->Divide((TH1F*)(_file0->Get("h1_taufakerate_ptjet3_den")));
((TH1F*)(_file0->Get("h1_taufakerate_ptjet3_eff")))->Draw();
((TH1F*)(_file0->Get("h1_taufakerate_ptjet3_eff")))->GetXaxis()->SetRange(0,5);

c->SaveAs("taufakerate_ptjet3_eff.png");

((TH1F*)(_file0->Get("h1_taufakerate_ptjet4_num")))->Clone("h1_taufakerate_ptjet4_eff");
((TH1F*)(_file0->Get("h1_taufakerate_ptjet4_eff")))->Divide((TH1F*)(_file0->Get("h1_taufakerate_ptjet4_den")));
((TH1F*)(_file0->Get("h1_taufakerate_ptjet4_eff")))->Draw();
((TH1F*)(_file0->Get("h1_taufakerate_ptjet4_eff")))->GetXaxis()->SetRange(0,5);
c->SaveAs("taufakerate_ptjet4_eff.png");

c->SetLogy(false);
c->Clear();
((TH1F*)(_file0->Get("h1_taufakerate_jetrank_num")))->Clone("h1_taufakerate_jetrank_eff");
((TH1F*)(_file0->Get("h1_taufakerate_jetrank_eff")))->Divide((TH1F*)(_file0->Get("h1_taufakerate_jetrank_den")));
((TH1F*)(_file0->Get("h1_taufakerate_jetrank_eff")))->GetYaxis()->SetRangeUser(0.,0.0004);
((TH1F*)(_file0->Get("h1_taufakerate_jetrank_eff")))->Draw();
c->SaveAs("taufakerate_jetrank_eff.png");

c->Clear();
((TH2F*)(_file0->Get("h2_taufakerate_num")))->Clone("h2_taufakerate_eff");
((TH2F*)(_file0->Get("h2_taufakerate_eff")))->Divide((TH2F*)(_file0->Get("h2_taufakerate_den")));
((TH2F*)(_file0->Get("h2_taufakerate_eff")))->SetStats(false);
((TH2F*)(_file0->Get("h2_taufakerate_eff")))->Draw("colz,text");
((TH2F*)(_file0->Get("h2_taufakerate_eff")))->GetXaxis()->SetRange(0,5);
c->SetLogz();
c->SaveAs("taufakerate_eff.png");

cout<<"end"<<endl;

}

