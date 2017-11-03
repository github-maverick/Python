class Parent:
	def func(self):
		print("This is a parent function.")

class Child(Parent):
	def func(self):
		print("This is a child function.")


c= Child()
c.func() #same func() function in child and Parent class so it overrides it
