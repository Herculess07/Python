class Student:
	# Constructor
	def __init__(self, enrolment_number, name, city):
		self.enrolment_number = enrolment_number
		self.name = name
		self.__city = city

	def details(self):
		print("Name : ", self.name)
		print("Enrolment Number : ", self.enrolment_number)

	def city_details(self):
		print("City : ", self.__city)


std = Student(22084231029, "Shreya", "Visnagar")

std.details()
std.city_details()