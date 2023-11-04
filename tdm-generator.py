#!/usr/bin/env python3
import sys
import os
import copy

def read_filenames(path):
	"""
	Precondition: path is the location of a directory containing input files in the required format
	Returns: a list containing the names of all files in the directory
	"""
	filenames = []
	# os.listdir gives the names of all files in a directory
	for filename in os.listdir(path):
		filenames.append(filename)
	return filenames

def read_terms_and_frequencies(path):
	"""
	Precondition: path is the location of a file to get terms from
	Returns: a dictionary where the keys are terms and the values are frequencies
	"""
	terms = {}
	with open(path,"r") as f:
		lines = f.readlines()
	for line in lines:
		# knowing that files are formatted as a term, a space, and a frequency, we can split the string
		line = line.split(" ")
		terms[line[0]] = line[1]
	return terms

def combine_keys_from_dicts(dict_list):
	"""
	Precondition: dict_list is a list of dictionaries where the keys are terms and the values are frequencies
	Returns: a list of keys
	"""
	terms = []

	for d in dict_list:
		for term in d.keys():
			if term not in terms:
				terms.append(term)
	return terms

def write_list_to_file(l, path):
	"""
	Precondition: l is a list. path is the location of a file to be created.
	Prints each element of the list
	"""
	s = ""
	for line in l:
		s += str(line) + "\n"
	with open(path,"w") as f:
		f.write(s)

def write_matrix_to_file(m, terms, path):
	"""
	Precondition: m is a list of dictionaries: each dictionary represents a file, the keys are terms and the values are frequencies. path is the location of a file to be created.
	Prints the values from the dictionaries in a table
	"""
	# len(terms) is the number of rows and len(m) is the number of columns
	s = str(len(terms)) + " " + str(len(m)) + "\n"
	for term in terms:
		for column in m:
			if term in column:
				s += column[term].strip() + " "
			else:
				s += "0 "
		s = s[:-1] + "\n"
	with open(path,"w") as f:
		f.write(s)


def main():
	# ensure that there are enough command-line arguments
	if len(sys.argv) < 3:
		print("Not enough arguments.\nThis program requires a path to an input directory and a path to an output directory.")
		sys.exit()
	# create the output folder
	if not os.path.exists(sys.argv[2]):
		os.makedirs(sys.argv[2])
	
	# make sorted_documents.txt
	filenames = read_filenames(sys.argv[1])
	filenames.sort()
	write_list_to_file(filenames, os.path.join(sys.argv[2],"sorted_documents.txt"))
	
	# make sorted_terms.txt and td_matrix.txt
	terms_and_frequencies = []
	for filename in filenames:
		terms_and_frequencies.append(read_terms_and_frequencies(os.path.join(sys.argv[1],filename)))
	terms = combine_keys_from_dicts(terms_and_frequencies)
	terms.sort()
	write_list_to_file(terms, os.path.join(sys.argv[2],"sorted_terms.txt"))
	write_matrix_to_file(terms_and_frequencies, terms, os.path.join(sys.argv[2],"td_matrix.txt"))

if __name__ == "__main__":
	main()
