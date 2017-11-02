class students:
	def __init__(self, name, sex, age, grade):
		self.name=name
		self.age=age
		self.grade=grade
		self.sex=sex

	def displaystudent(self):
		if self.sex=="Male":
			s="his"
		else:
			s="her"
		return("Student's name is {} and {} age is {}.".format(self.name, s, self.age))

stud1= students("Ram","Male", 12, "7th")
stud2= students("Sita","Female", 13, "8th")
print(stud1.displaystudent())
print(stud2.displaystudent())



