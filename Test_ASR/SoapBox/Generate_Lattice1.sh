#!/bin/bash
# Given the test feature vector in appropriate shape, we can use the acoustic model and decoding graph to generate lattices of hypothesized transcriptions. 

# Inputs
#	1. Word-to-symbol table
#	2  Trained acoustic model 
#       3. Decoding graph 
#       4. Features
# Ouput
#	1 Lattice File
./kaldi/src/nnet2bin/nnet-latgen-faster --min-active=1000 --max-active=7000 --beam=15.0 --lattice-beam=1.0 --acoustic-scale=0.1 --allow-partial=true --word-symbol-table=./exp/DNN/graph/words.txt ./exp/DNN/final.mdl ./exp/DNN/graph/HCLG.fst ark:./data/test/feats.ark "ark:|gzip -c > ./exp/DNN/decode/lat.1.gz"
