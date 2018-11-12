#!/bin/bash
declare -i count=0
for filename in ./data/*.txt; do
  echo $count,$filename
  python3 runner.py < $filename
  printf "\n"
  count=count+1
done

