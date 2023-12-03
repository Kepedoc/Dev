#!/bin/bash

number=$((1 + RANDOM % 81))

line=$(sed "${number}q;d" "quotes.txt")

echo $line
