# 19 Get the key of a minimum value from the following dictionary
marks = {
	"Python": 56,
	"Android": 59,
	"CDP2": 51,
	"NoSql": 60
}

min_value = min(marks, key=marks.get)
print(min_value)
