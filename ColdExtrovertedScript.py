#Start code here
from turtle import *
turtle = Turtle()
screen = Screen()
turtle.speed(0)
for i in range(24):
  for i in range(3):
    turtle.forward(90)
    turtle.left(120)
  turtle.right(15)
screen.mainloop()

