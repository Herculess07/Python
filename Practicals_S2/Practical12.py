# 12 Write a program to check if the given file is empty or not

import os

# Checking that file is empty or not
fileSize = os.path.getsize("first.txt")
if fileSize == 0:
	print("file is empty")
else:
	print("file is not empty")

# for checking path is exist or not
pathExist = os.path.exists("../output.txt")

if pathExist:
	print("yes file exist")
