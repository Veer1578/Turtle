import turtle
turtle.Screen().bgcolor("aqua")
turtle.Screen().title("Turtle")
my_pen = turtle.Turtle()
size = 0
while True:
    for i in range(4):
        my_pen.forward(size + 1)
        my_pen.left(90)
        size -= 5
    size += 1

turtle.done()
