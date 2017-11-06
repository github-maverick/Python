import turtle

my_turtle=turtle.Turtle()
my_turtle.speed(0)

def square(x,y):
	for i in range(4):
		my_turtle.forward(x)
		my_turtle.right(90)
	my_turtle.right(y)

for q in range(150):
	square(150,11)

