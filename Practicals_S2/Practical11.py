# 11 Write all content of a given file into a new file by skipping line number 5

# Open the input file for reading
with open("first.txt", "r") as input_file:
	# Read all lines from the first file
	lines = input_file.readlines()

# Open the output file for writing
with open("../output.txt", "w") as output_file:
	# Iterate over the lines, excluding line number 5
	for index, line in enumerate(lines):
		if index != 4:  # Skip line number 5 (index is zero-based)
			output_file.write(line)
