#!/bin/bash
# run after running create_all_directories.sh

for url in `cat processed-results.txt`
do
	cd hierarchy

	# determine protocol, so it can be removed with substrings
	if [[ $url == https://* ]]; then
		# for index pages, add index.html
		if [[ $url == */ ]]; then
			curl $url > "${url:8}""index.html"
		# for plaintext pages, use extension
		elif [[ $url == *.html  ]] || [[ $url == *.txt  ]]; then
			curl $url > "${url:8}"
		# for dynamic pages, add .html
		elif [[ $url == *.php  ]] || [[ $url == *.perl ]] || [[ $url == *.py ]]
		then
			curl $url > "${url:8}"".html"
		else
			echo "$url"" has unexpected file type"
		fi
	elif [[ $url == http://* ]]; then	
		# for index pages, add index.html
		if [[ $url == */ ]]; then
			curl $url > "${url:7}""index.html"
		# for plaintext pages, use extension
		elif [[ $url == *.html  ]] || [[ $url == *.txt  ]]; then
			curl $url > "${url:7}"
		# for dynamic pages, add .html
		elif [[ $url == *.php  ]] || [[ $url == *.perl ]] || [[ $url == *.py ]]
		then
			curl $url > "${url:7}"".html"
		else
			echo "$url"" has unexpected file type"
		fi	
	else
		echo $url" has unexpected protocol"
	fi

	cd .. 
done
