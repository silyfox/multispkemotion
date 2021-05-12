#!/bin/bash

for id in `cat id.txt`; do
	cp ../Baseline_decoder/wav_melgan/$id* baseline/
	cp ../GST_add_cls_mean/wav_melgan/$id* proposed/
done
