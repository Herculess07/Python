# Write a program to rename a key city to a location in the following dictionary.
# Given:
sample_dict = {
	"city": "Mehsana"
}

# method1
sample_dict["location"] = sample_dict.pop("city")

# method2
'''
sample_dict["location"] = sample_dict["city"]
del sample_dict["city"]
'''
print(sample_dict)
