#!/bin/bash

WAIT=0
if [ -z $1 ]; then
    if [[ "$(date +%H)" -eq "23" ]]; then
        DATE=$(date -d tomorrow +%d)
        WAIT=1
    else
        DATE=$(date +%d)
    fi
else
    DATE=$1
fi

if [ -d "day${DATE}" ]; then
    echo "Already initialized"
    exit 1
fi

mkdir "day$DATE"
cp template.py day$DATE/solution.py
touch day$DATE/test.txt
code day$DATE/solution.py

if [[ $WAIT -eq 1 ]]; then
    aocdl -wait
else
    aocdl -day $DATE
fi