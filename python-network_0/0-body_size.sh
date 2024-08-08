#!/bin/bash
# Script to handle two different expected GET response outputs
resp=$(curl -s "$1"); [ "$resp" == "my index page" ] && echo "Correct output: GET / => “$resp Mainly because it’s in Python”"
