#!/usr/bin/env bash

args=("$@")


if [[ "${args[0]}" == "clean" ]]; then
    rm /Users/drewskikatana/titan/test/*
    echo "folder cleaned"
fi

if [[ "${args[0]}" == "count" ]]; then
TOTAL=0
FILES="/Users/drewskikatana/titan/test/*"
for f in $FILES
do
    TOTAL=$(( TOTAL + 1 ))
done
echo $TOTAL
fi