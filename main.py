import turtle

pen = turtle.Turtle()
turtle.colormode(255)
turtle.Screen().bgcolor("pink")
pen.color("white")
pen.speed(0)
pen.width(5)
pen.fillcolor("pink")
pen.begin_fill()
for i in range(3):
    pen.forward(400)
    pen.right(90)
pen.end_fill()
for i in range(200):
    red = 28 + int((i * 0.8))  # 190
    green = 5 + int((i * 0.6))  # 156
    blue = 71 + int((i * 0.9))  # 255
    pen.width(26 - (i / 8))
    pen.color(red, green, blue)
    print(red, green, blue)
    for i in range(3):
        pen.forward(400)
        pen.right(90)
pen.hideturtle()
turtle.done()
