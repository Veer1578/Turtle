import turtle
num_sides = 4
turtle.Screen().bgcolor("white")
turtle.Screen().setup(300, 400)
polygon = turtle.Turtle()  # Stores position of turtle

length = 70
angle = 360.0/num_sides
for i in range(num_sides):
    polygon.forward(length)
    polygon.right(angle)
turtle.done()
