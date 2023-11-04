#!/bin/bash
# run after running preprocess.sh

if [[ -d hierarchy ]]; then
	rm -r hierarchy 
fi

mkdir hierarchy
OLDIFS=$IFS

# Iterate through urls in the crawler results
for url in `cat processed-results.txt`
do
	# make a directory in hierarchy	for the url
	IFS="/"
	set $url
	if [ ! -d hierarchy/$3 ]; then
		mkdir hierarchy/$3
	fi
	IFS=$OLDIFS
done



IFS=$OLDIFS


