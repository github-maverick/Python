class students:
	def __init__(self, name, age, grade):
		self.name=name
		self.age=age
		self.grade=grade

stud1= students("Ram", 12, "7th")
stud2= students("Rita", 13, "8th")
setattr(stud1, "address", "Parsa") #sets a new attribute to an object
print(stud1.name)
print(stud1.age)
print(stud1.grade)
print(hasattr(stud1, "address")) #boolean operator to check if the object has the given attribute
print(getattr(stud1, "address" )) #it is same as stud1.address
delattr(stud1, "address") # to delete an attribute
print(hasattr(stud1, "address"))
