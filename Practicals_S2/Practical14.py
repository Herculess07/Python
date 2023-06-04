# Merge two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}


# Python code to merge dict using update() method
# def Merge(dict1, dict2):
# 	return (dict2.update(dict1))


# Driver code
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict_sum = {**dict1, **dict2}

# print(dict1 | dict2)
print(dict_sum)

# This returns None
# print(Merge(dict1, dict2))

# changes made in dict2
# print(dict2)
