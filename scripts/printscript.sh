#!/bin/bash

echo "begin"

rm -rf input_weighted/output

mkdir input_weighted/output
mkdir input_weighted/output/jetpt
mkdir input_weighted/output/jet1pt
mkdir input_weighted/output/jet2pt
mkdir input_weighted/output/taufakerate_pt_eff
mkdir input_weighted/output/taufakerate_ptjet1_eff
mkdir input_weighted/output/taufakerate_ptjet2_eff
mkdir input_weighted/output/taufakerate_ptjet3_eff
mkdir input_weighted/output/taufakerate_ptjet4_eff
mkdir input_weighted/output/taufakerate_jetrank_eff
mkdir input_weighted/output/taufakerate_eff

for name in `cat filetoplotlist.txt`;
do

echo "Printing plots for $name "
root -l input_weighted/$name.root -q -x effmap_printmacro.C
mv jetpt.png input_weighted/output/jetpt/jetpt_$name.png
mv jet1pt.png input_weighted/output/jet1pt/jet1pt_$name.png
mv jet2pt.png input_weighted/output/jet2pt/jet2pt_$name.png
mv taufakerate_pt_eff.png input_weighted/output/taufakerate_pt_eff/taufakerate_pt_eff_$name.png
mv taufakerate_ptjet1_eff.png input_weighted/output/taufakerate_ptjet1_eff/taufakerate_ptjet1_eff_$name.png
mv taufakerate_ptjet2_eff.png input_weighted/output/taufakerate_ptjet2_eff/taufakerate_ptjet2_eff_$name.png
mv taufakerate_ptjet3_eff.png input_weighted/output/taufakerate_ptjet3_eff/taufakerate_ptjet3_eff_$name.png
mv taufakerate_ptjet4_eff.png input_weighted/output/taufakerate_ptjet4_eff/taufakerate_ptjet4_eff_$name.png
mv taufakerate_jetrank_eff.png input_weighted/output/taufakerate_jetrank_eff/taufakerate_jetrank_eff_$name.png
mv taufakerate_eff.png input_weighted/output/taufakerate_eff/taufakerate_eff_$name.png

done

echo "end"
