#!/bin/bash
# run after running setup_hierarchy.sh

OLDIFS=$IFS

for url in `cat processed-results.txt`
do
	# tokenize url
	IFS="/"
	set $url
	IFS=$OLDIFS
	
	# iterate through standard variables
	path="$3"
	for (( i=4 ; i<$#; i ++ ))
	do
		path="$path/${!i}"
	done	
	
	if [[ $url == */ ]]; then
		[[ i++ ]]
		path="$path/${!i}"
	fi
	
	echo $path
	
	# make directories
	cd hierarchy
	mkdir -p $path
	cd ..	
done
