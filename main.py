import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("yellow")
t = turtle.Turtle()

t.setheading(135)
t.penup()
t.goto(0,0)
t.pendown()
t.pencolor("cyan")
t.fillcolor("cyan")
t.begin_fill()
t.speed(1)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()


t.pencolor("brown")
t.fillcolor("brown")
t.begin_fill()
t.speed(1)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.end_fill()

t.hideturtle()






turtle.done()
