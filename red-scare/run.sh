#!/bin/bash
declare -i count=0
for filename in ./data/*.txt; do
  python3 runner.py $filename < $filename
  count=count+1
done

