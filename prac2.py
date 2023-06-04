# import os
# File Handling in Python
'''
# x (Create) - if file exist - error
# r (Read)- if file Don't exist - error
# w (Write)- write in file no error
# a (Append)- appending 
''' 
# For creating new file
'''
file = open("first.txt","x")
'''

# For read and prints data what read
'''
file = open("first.txt","r")
print(file.read())
print(file.readline())
file.close()
'''

# For Write data inside file 
'''
file = open("first.txt","w")
file = open("first.txt","a")
file.write("hello woodifdd ")
file.close()
'''
 
# For Print whole file use loop
'''
file = open("first.txt","r") 
for x in file:
    print(x)
'''   

'''
write_file = open("Delete.txt","w")
write_file.write("This is file created for Practice remove function from os")

read_file = open("Delete.txt","r")
print(read_file.read())
'''
# read_file.close()

# For Deleting filr using os module
'''
os.remove("Delete.txt")
print("File deleted")
'''