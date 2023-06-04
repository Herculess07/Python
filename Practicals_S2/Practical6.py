"""
p6: Concatenate two lists index-wise
For ex.
list1=[“I”, “a”, “from”, “Semester”]
list2=[“am”, “student”,”” M.Sc. (CA & IT)”,” 2”]
Output: I am a student from M.Sc.(CA & IT Semester 2.
Hint: use zip() function
"""

list1 = ["I", "a", "from", "Semester"]
list2 = ["am", "student", "M.Sc. (CA & IT)", "2"]

lis = " ".join([w1 + " " + w2 for w1, w2 in zip(list1, list2)])
print(list)

