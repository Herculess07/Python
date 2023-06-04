# 28 Write a Python program to count the frequency of words in a file use appropriate exception handling mechanism

from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("first.txt"))

with open("first.txt","r") as f:
	list1= []
	list1 = f.read().split()
#
	wordFrequency = [list1.count(p) for p in list1]
	print("frequency of words : ")
	print(dict(zip(list1,wordFrequency)))