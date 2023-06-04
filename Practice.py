string = "Palanpur"

for x in string:
	print(x)

# length of string
print(len(string))

# Checking certain word in string
print("p" in string)

# Checking if certain word is not in string
print("l" not in string)

# slicing in string
string2 = "This is string in python"
print(string2[2:5])
print(string2[:5])
print(string2[8:])

# negative indexing
string3 = "it's cloudy weather"
print(string3[-8:-2])
print(string3.upper())
print(string3.lower())

# remove whitespace
string4 = "      hello world       "
print(string4)
print(string4.strip())
print(string4.replace("hello","hii"))
print(string4.replace("hello","hii").strip())
print(string4.split(" "))

