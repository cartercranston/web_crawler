#!/bin/bash
# put the list of webpages in a file called crawler-results.txt, 
#  then run

grep -f extensions.txt -v crawler-results.txt > processed-results.txt
