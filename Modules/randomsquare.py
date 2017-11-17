import turtle
m=turtle.Turtle()
from random import randint
y=400
m.speed(0)
while y>0:
  for x in range(4):
    m.forward(y)
    m.left(90)

  y-=randint(2,15)
