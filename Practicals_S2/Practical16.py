# Write a program to Delete a list of keys from a dictionary
# Book = {
# 	"Author": "Dell Karnigi",
# 	"Name": "Atomic Habits",
# 	"Price": 594,
# 	"Published Year": "1998",
# 	"Pages": 234,
# 	"Read Pages": 32,
# 	"Price Drops": -33,
# 	"Sells Partner": "Flipkart",
# 	"Sells Partner2": "Amazon",
# 	"Sells Partner3": "eBay"
# }

dict1 = {
	'a': 1,
	'b': 2,
	'c': 3,
	'd': 4,
	'e': 5,
	'f': 6,
	'g': 7
}
keys = ['a','b','c']

for key in keys:
	dict1.pop(key)

print(dict1)
