#!/bin/bash
for filename in ./data/*.txt; do
  time python3 runner.py < $filename
done

