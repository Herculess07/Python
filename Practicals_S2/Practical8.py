# 8 Remove all occurrences of a specific item from a list

vegetables = ["Gaubi Flower", "Ladies Finger", "Potato", "Potato", "Tomato", "Potato", "Onion", "Radish"]
print("Before Remove :", vegetables)

remVeg = str(input("Enter Vegetable Name for Remove : "))

while remVeg in vegetables:
	vegetables.remove(remVeg)
	print(f"After Removed {remVeg}: {vegetables}")

if(remVeg not in vegetables):
	print("Enter Write Value")

