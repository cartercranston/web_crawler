#!/usr/bin/env python3
import sys
import os

def read_file_to_list(path):
	"""
	Precondition: path is to a text file
	Returns: A list containing each line of the file
	"""
	file_contents = []
	lines = []
	with open(path, "r") as f:
		lines = f.readlines()
	for line in lines:
		file_contents.append(line.strip())

	return file_contents

def read_file_to_matrix(path):
	"""
	Precondition: path is to a text file where all lines but the first create a matrix of integers
	Returns: A list of lists containing the integers from the matrix
	"""
	matrix = []
	lines = []
	with open(path, "r") as f:
		lines = f.readlines()
	# Remove the first line, which isn't part of the matrix
	lines = lines[1:]
	# Add numbers to the correct row and column of matrix
	for line in lines:
		row = []
		for num in line.split():
			row.append(num)
		matrix.append(row)
	return matrix

def get_vector_from_stdin(sorted_terms):
	"""
	Precondition: sorted_terms is a list of strings. Each line in stdin consists of a word, a space, and an integer
	Returns: A list of integers, the frequency (in stdin) of each of the terms (in sorted_terms)
	"""
	stdin_dict = {}
	vector = []

	for line in sys.stdin:
		# if the precondition is true, line[0] is a term and line[1] is its frequency
		line = line.split()
		stdin_dict[line[0]] = line[1]

	# fill vector according to the order of sorted_terms
	for term in sorted_terms:
		vector.append(stdin_dict.get(term, 0))

	return vector

def vector_similarity(vector1, column, matrix):
	"""
	Precondition: vector1 is a list of integers. column is an integer corresponding to a column of matrix. matrix is a list of lists of integers.
	Returns: a float, the cosine of the angle between vector1 and the given column of matrix.
	"""
	# the cosine of the angle between two vectors is equal to their dot product divided by each of their magnitudes
	# the dot product of two vectors u and v is given by Sigma(u[i] * v[i])
	dot_product = 0
	# the magnitude of a vector is the square root of its dot product with itself
	v1_sq_magnitude = 0
	v2_sq_magnitude = 0

	for i in range(len(vector1)):
		v1_sq_magnitude += float(vector1[i]) ** 2
		v2_sq_magnitude += float(matrix[i][column]) ** 2
		dot_product += float(vector1[i]) * float(matrix[i][column])
	v1_magnitude = v1_sq_magnitude ** 0.5
	v2_magnitude = v2_sq_magnitude ** 0.5
	return dot_product / (v1_magnitude * v2_magnitude)

def main():
	# get data from tdm-generator
	sorted_terms = read_file_to_list(os.path.join(sys.argv[1],"sorted_terms.txt"))
	filenames = read_file_to_list(os.path.join(sys.argv[1],"sorted_documents.txt"))
	matrix = read_file_to_matrix(os.path.join(sys.argv[1],"td_matrix.txt"))

	# get query from stdin and convert it to a vector
	query_vector = get_vector_from_stdin(sorted_terms)

	# rank all files by their similarity to the query
	similarities = {}
	for i in range(len(filenames)):
		similarities[filenames[i]] = vector_similarity(query_vector, i, matrix)

	filename_ranking = sorted(similarities,key=similarities.get)
	filename_ranking.reverse()

	# print out the ranking
	for filename in filename_ranking:
		print("%.4f %s" % (similarities[filename], filename))
	

if __name__ == "__main__":
	main()
