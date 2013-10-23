#!/bin/bash

echo "..done"
echo "Start merging files"

hadd allDY.root DY*.root

hadd allHiggs.root HT*.root

cp TTJets_MassiveBinDECAY.root allTTbar.root

hadd alldata.root Tau*.root

hadd allsignal.root VBFSUSY*.root

hadd allVV.root ZZ*.root WmWmqq.root WpWpqq.root WZ*.root WW_DoubleScattering.root WWjjTo2L2Nu_8TeV.root

cp WJetsToLNu_TuneZ2Star.root allW.root

echo "File merging COMPLETE!!!"

echo "Job Done!!!"

