#!/bin/bash

DATE="${1:-$(date -d tomorrow +%d)}"

if [ -d "day${DATE}" ]; then
    echo "Already initialized"
    exit 1
fi

mkdir "day$DATE"
cp template.py day$DATE/solution.py

if [ -z $1 ]; then
    aocdl -wait
else
    aocdl -day $DATE
fi