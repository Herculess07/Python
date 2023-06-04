# 21 Write a program to count occurrences of all characters within a string
sentence = "aaaa bbbb fff d ggg kkkkkkk nnn mmm nn bbb"
char = dict()
for word in sentence:
	count = sentence.count(word)
	char[word] = count

print(f"Answer : {char}")

