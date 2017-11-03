class parent:
	counter=10
	hit=15
	def __init__(self):
		print("Parent class initialized.")
	def SetCounter(self, num):
		self.counter= num


class child(parent): # child is the child class of Parent
	def __init__(self):
		print("Child class being initialized.")
	def SetHit(self, num2):
		self.hit=num2
c= child()
print(c.counter)
c.SetCounter(20)
print(c.counter)
print(c.hit)
c.SetHit(30)
print(c.hit)

