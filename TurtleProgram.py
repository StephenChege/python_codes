#A turtle program to display a letter ‘V’

import turtle

t = turtle.Turtle()
t.penup()
t.goto(-60,0)
t.pendown()
t.color('black')
style = ('Courier', 70)
t.write("'V'", font=style)
t.hideturtle()
