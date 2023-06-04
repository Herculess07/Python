# 5 Count the total number of digits in a number

num = int(input("Enter Number For Count : "))
count = 0

while num != 0:
    num //= 10
    count += 1

print(f"number of digits : {str(count)}")
