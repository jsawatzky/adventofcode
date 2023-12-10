#!/bin/bash

DATE="$(date +%d)"
INFILE="input.txt"
while getopts "td:" option; do
    case $option in
        t)
            INFILE="test.txt"
            ;;
        d)
            DATE="$OPTARG"
            ;;
        \?)
            echo "Invalid option"
            exit 1;;
    esac
done

if [ ! -d "day${DATE}" ]; then
    echo "No solution found"
    exit 1
fi

python3.9 day$DATE/solution.py day$DATE/$INFILE