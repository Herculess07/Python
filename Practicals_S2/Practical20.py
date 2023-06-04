# 20 Write a program to find all occurrences of “DCS” in a given string ignoring the case.
# Given: “Hi This is DCS, DCS means Department of Computer Science, Ganpat University”

sentence = "Hi This is DCS, DCS means Dcs Department of Computer Science, Ganpat University"
word = "DCS"

sentence_lower = sentence.lower()
word_lower = word.lower()

print(sentence_lower.count(word_lower))


