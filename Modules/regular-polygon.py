n=int(input("Number of sides of polygon: "))
length=int(input("Length of each sides(in pixel): "))
angle=(360/n)
import time
import turtle
m=turtle.Turtle()
for x in range(n):
	m.forward(length)
	m.left(angle)
time.sleep(2)

