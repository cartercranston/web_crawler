#!/usr/bin/env python3
import sys

def main():
	terms = create_dict()
	print_dict(terms)

def create_dict():
	"""
	Purpose: Reads the standard input, and counts how many times each word appears
	Returns: A dictionary where the keys are the words in standard input, and the values are the number of times those words appear
	"""
	terms = {}
	for line in sys.stdin:
		for term in line.split():
			# If the key already exists, its value needs to be incremented
			if term in terms:
				terms[term] += 1
			# if the key doesn't exist, it should be added to the dictionary
			else:
				terms[term] = 1
	return terms

def print_dict(terms):
	"""
	Purpose: Prints each key-value pair on a separate line, in alphabetic order of keys
	Precondition: terms is a dictionary
	"""
	for term, count in sorted(terms.items()):
		# print automatically adds a space between arguments
		print(term, count)

if __name__ == "__main__":
	main()
