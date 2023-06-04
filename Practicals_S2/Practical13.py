# 13 Read line number 4 from the specific file
import linecache

with open("first.txt", "r") as input_file:
	lines = input_file.readlines()

for index, line in enumerate(lines):
	if index == 3:
		print(line)


line = linecache.getline("first.txt", 4)
print(line)
