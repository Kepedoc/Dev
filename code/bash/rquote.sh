#!/bin/bash

while true; do 

    number=$((1 + RANDOM % 81))
    line=$(sed "${number}q;d" "quotes.txt")
    echo $lines
    sleep 1m
done
