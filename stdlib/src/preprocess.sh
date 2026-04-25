#!/usr/bin/bash
cd "$(dirname "$0")"
cp *.emlprg ../
python3 ../../preprocess.py ../*.emlprg
