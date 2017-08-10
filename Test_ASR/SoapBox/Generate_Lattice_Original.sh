#!/bin/bash
# Given the test feature vector in appropriate shape, we can use the acoustic model and decoding graph to generate lattices of hypothesized transcriptions. 

# Inputs
#	1. Word-to-symbol table
#	2  Trained acoustic model 
#       3. Decoding graph 
#       4. Features
# Ouput
#	1 Lattice File
/home/abraham/Speech_Recognition/kaldi/src/nnet2bin/nnet-latgen-faster --word-symbol-table=/home/abraham/Speech_Recognition/kaldi/egs/SoapBox/exp/DNN/graph/words.txt /home/abraham/Speech_Recognition/kaldi/egs/SoapBox/exp/DNN/final.mdl /home/abraham/Speech_Recognition/kaldi/egs/SoapBox/exp/DNN/graph/HCLG.fst ark:/home/abraham/Speech_Recognition/kaldi/egs/SoapBox/data/test/feats.ark "ark:|gzip -c > /home/abraham/Speech_Recognition/kaldi/egs/SoapBox/exp/DNN/decode/lat.1.gz"
