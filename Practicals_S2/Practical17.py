# Write a Python program to check if value 200 exists in the following dictionary.
# sample_dict = {'a': 100, 'b': 200, 'c': 300}

sample_dict = {'a': 100, 'b': 200, 'c': 300}

check_value = 200 in sample_dict.values()
print(check_value)

check_key = "a" in sample_dict.keys()
print(check_key)
