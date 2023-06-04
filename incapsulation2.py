# base class
class Subject:
    def __init__(self):
        # Protected member
        self._subject2 = "DMM/SEO"
        self._subject3="Python"

# child class
class Student(Subject):
    def __init__(self, name,enrolment):
        self.name = name
        self.enrolment=enrolment
        Subject.__init__(self)

    def show(self):
        print("Student name :", self.name)
        # Accessing protected member in child class
        print("Elective Subject 2 :", self._subject2)
        print("Elective Subject 3 :", self._subject3)

c = Student("Chaudhary Akash Alpeshbhai",22084231036)
c.show()

# Direct access protected data member
print('Project:', c._subject2)