import turtle
m=turtle.Turtle()
m.speed(0)
def square():
    for x in range(4):
        m.forward(100)
        m.right(90)
for x in range(500):
    square()
    m.right(11)
