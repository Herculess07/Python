# Exception Handling in Python

i = 10
try:
    print(i/0)
except ArithmeticError:
    print("This is ArithmeticError")
except ZeroDivisionError:
    print("zero division error occoured")
except:
    print("Error occour while executing..")

else:
    print("Successful..")
