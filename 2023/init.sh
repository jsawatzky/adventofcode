#!/bin/bash

DATE="${1:-$(date -d tomorrow +%d)}"
if [ -z $1 ]; then
    if [[ "$(date +%H)" > "23" ]]; then
        DATE=$(date -d tomorrow +%d)
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
code day$DATE/solution.py

if [ -z $1 ]; then
    aocdl -wait
else
    aocdl -day $DATE
fi