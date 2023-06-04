# Remove empty strings from the list of strings

strings = ["string0", "string1", "", "string2", "", "string3"]

print("before : " + str(strings))

while "" in strings:
    strings.remove("")

print("after : " + str(strings))
