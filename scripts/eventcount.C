#include <TROOT.h>
#include <TDirectory.h>
#include <TCanvas.h>
#include <TFile.h>
#include <TH1F.h>
#include <iostream>
#include <cmath>

using namespace std;

void eventcount(TFile* inputfile){

TH1F* h1_SRcounts = ((TH1F*)(inputfile->Get("SignalRegion/counts")));
TH1F* h1_CR2counts = ((TH1F*)(inputfile->Get("Central_invertedVBF_2TightIso_CR2/counts")));
TH1F* h1_CR3counts = ((TH1F*)(inputfile->Get("Central_1TightIso_CR3/counts")));
TH1F* h1_CR4counts = ((TH1F*)(inputfile->Get("Central_invertedVBF_1TightIso_CR4/counts")));
TH1F* h1_CR5counts = ((TH1F*)(inputfile->Get("Central_AntiTightIso_CR5/counts")));
TH1F* h1_CR6counts = ((TH1F*)(inputfile->Get("Central_invertedVBF_AntiTightIso_CR6/counts")));
TH1F* h1_CR7counts = ((TH1F*)(inputfile->Get("Central_AntiMediumIso_CR7/counts")));
TH1F* h1_CR8counts = ((TH1F*)(inputfile->Get("Central_invertedVBF_AntiMediumIso_CR8/counts")));
TH1F* h1_CR9counts = ((TH1F*)(inputfile->Get("Central_AntiLooseIso_CR9/counts")));
TH1F* h1_CR10counts = ((TH1F*)(inputfile->Get("Central_invertedVBF_AntiLooseIso_CR10/counts")));


double SRcounts = h1_SRcounts->GetBinContent(11);
double CR3counts = h1_CR3counts->GetBinContent(13);
double CR5counts = h1_CR5counts->GetBinContent(13);
double CR7counts = h1_CR7counts->GetBinContent(13);
double CR9counts = h1_CR9counts->GetBinContent(13);

double SRcounts_err = 0.;
double CR3counts_err = 0.;
double CR5counts_err = 0.;
double CR7counts_err = 0.;
double CR9counts_err = 0.;

if (SRcounts > 0.) SRcounts_err = sqrt(SRcounts);
if (CR3counts > 0.) CR3counts_err = sqrt(CR3counts);
if (CR5counts > 0.) CR5counts_err = sqrt(CR5counts);
if (CR7counts > 0.) CR7counts_err = sqrt(CR7counts);
if (CR9counts > 0.) CR9counts_err = sqrt(CR9counts);

double CR2counts = 0;
double CR4counts = 0;
double CR6counts = 0;
double CR8counts = 0;
double CR10counts = 0;

for (int i = 7; i < 15; i++){

	CR2counts += h1_CR2counts->GetBinContent(i);
	CR4counts += h1_CR4counts->GetBinContent(i);
	CR6counts += h1_CR6counts->GetBinContent(i);
	CR8counts += h1_CR8counts->GetBinContent(i);
	CR10counts += h1_CR10counts->GetBinContent(i);

}

double CR2counts_err = 0.;
double CR4counts_err = 0.;
double CR6counts_err = 0.;
double CR8counts_err = 0.;
double CR10counts_err = 0.;

if (CR2counts > 0.) CR2counts_err = sqrt(CR2counts);
if (CR4counts > 0.) CR4counts_err = sqrt(CR4counts);
if (CR6counts > 0.) CR6counts_err = sqrt(CR6counts);
if (CR8counts > 0.) CR8counts_err = sqrt(CR8counts);
if (CR10counts > 0.) CR10counts_err = sqrt(CR10counts);


double onetighteff = (double)CR3counts / (double)(CR3counts + CR4counts);
double antitighteff = (double)CR5counts / (double)(CR5counts + CR6counts);
double antimediumeff = (double)CR7counts / (double)(CR7counts + CR8counts);
double antilooseeff = (double)CR9counts / (double)(CR9counts + CR10counts);

double onetighteff_err = sqrt( pow(  (((double)CR4counts * CR3counts_err)/(pow(((double)CR3counts + (double)CR4counts),2.))), 2.)  + pow(  (((double)CR3counts * CR4counts_err)/(pow(((double)CR3counts + (double)CR4counts),2.))), 2.)    );
double antitighteff_err = sqrt( pow(  (((double)CR6counts * CR5counts_err)/(pow(((double)CR5counts + (double)CR6counts),2.))), 2.)  + pow(  (((double)CR5counts * CR6counts_err)/(pow(((double)CR5counts + (double)CR6counts),2.))), 2.)    );
double antimediumeff_err = sqrt( pow(  (((double)CR8counts * CR7counts_err)/(pow(((double)CR7counts + (double)CR8counts),2.))), 2.)  + pow(  (((double)CR7counts * CR8counts_err)/(pow(((double)CR7counts + (double)CR8counts),2.))), 2.)    );
double antilooseeff_err = sqrt( pow(  (((double)CR10counts * CR9counts_err)/(pow(((double)CR9counts + (double)CR10counts),2.))), 2.)  + pow(  (((double)CR9counts * CR10counts_err)/(pow(((double)CR9counts + (double)CR10counts),2.))), 2.)    );

double onetightbgpred = (double)CR2counts * (onetighteff / (1. - onetighteff) );
double antitightbgpred = (double)CR2counts * (antitighteff / (1. - antitighteff) );
double antimediumbgpred = (double)CR2counts * (antimediumeff / (1. - antimediumeff) );
double antiloosebgpred = (double)CR2counts * (antilooseeff / (1. - antilooseeff) );

double onetightbgpred_err = sqrt(  pow(   ((onetighteff * CR2counts_err)/( 1. - onetighteff))    , 2.)   +   pow(   (((double)CR2counts * onetighteff_err)/(pow( (1 - onetighteff) ,2.)))    , 2.)    );
double antitightbgpred_err = sqrt(  pow(   ((antitighteff * CR2counts_err)/( 1. - antitighteff))    , 2.)   +   pow(   (((double)CR2counts * antitighteff_err)/(pow( (1 - antitighteff) ,2.)))    , 2.)    );
double antimediumbgpred_err = sqrt(  pow(   ((antimediumeff * CR2counts_err)/( 1. - antimediumeff))    , 2.)   +   pow(   (((double)CR2counts * antimediumeff_err)/(pow( (1 - antimediumeff) ,2.)))    , 2.)    );
double antiloosebgpred_err = sqrt(  pow(   ((antilooseeff * CR2counts_err)/( 1. - antilooseeff))    , 2.)   +   pow(   (((double)CR2counts * antilooseeff_err)/(pow( (1 - antilooseeff) ,2.)))    , 2.)    );

cout << "#Event Counting#" << endl;
cout << "SR: "<< SRcounts  << " +- " << SRcounts_err <<endl;
cout << "CR2: "<< CR2counts  << " +- " << CR2counts_err <<endl;
cout << "CR3: "<< CR3counts  << " +- " << CR3counts_err <<endl;
cout << "CR4: "<< CR4counts  << " +- " << CR4counts_err <<endl;
cout << "CR5: "<< CR5counts  << " +- " << CR5counts_err <<endl;
cout << "CR6: "<< CR6counts  << " +- " << CR6counts_err <<endl;
cout << "CR7: "<< CR7counts  << " +- " << CR7counts_err <<endl;
cout << "CR8: "<< CR8counts  << " +- " << CR8counts_err <<endl;
cout << "CR9: "<< CR9counts  << " +- " << CR9counts_err <<endl;
cout << "CR10: "<< CR10counts  << " +- " << CR10counts_err<<endl;
cout << endl;
cout << "#VBF Efficency & BG Prediction#" << endl;
cout <<"One tight region-- "<<"VBF Efficency: "<< onetighteff << " +- "<<onetighteff_err<<" BG Prediction: " << onetightbgpred<< " +- "<< onetightbgpred_err << endl;
cout <<"Anti tight region-- "<<"VBF Efficency: "<< antitighteff << " +- "<<antitighteff_err<<" BG Prediction: " << antitightbgpred<< " +- "<< antitightbgpred_err << endl;
cout <<"Anti medium region-- "<<"VBF Efficency: "<< antimediumeff << " +- "<<antimediumeff_err<<" BG Prediction: " << antimediumbgpred<< " +- "<< antimediumbgpred_err << endl;
cout <<"Anti loose region-- "<<"VBF Efficency: "<< antilooseeff << " +- "<<antilooseeff_err<<" BG Prediction: " << antiloosebgpred<< " +- "<< antiloosebgpred_err << endl;

} 
