#!/bin/bash

DATE="${1:-$(date +%d)}"

if [ ! -d "day${DATE}" ]; then
    echo "No solution found"
    exit 1
fi

python3 day$DATE/solution.py day$DATE/input.txt