import turtle
pen=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor("white")
pen.color("red")
pen.width(10)
def createRING(clr,x,y):
 pen.color(clr)             
 pen.penup()
 pen.goto(x,y)
 pen.pendown()
 for i in range(36):
  pen.forward(5)            
  pen.right(10)
createRING("blue",-100,0)  