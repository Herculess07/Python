# 27 Write a Python program to count the number of lines in a text file use appropriate exception handling mechanism

with open("first.txt", 'r') as fp:
	lines = len(fp.readlines())
	print('Total Number of lines:', lines)
