import turtle
import random

t=turtle.Turtle()#pen
s=turtle.Screen()#paper

def firework(x,y,clr):
 t.penup()  
 t.goto(x,y)
 t.pendown()
 t.color(clr)
 for i in range(60):
   l=random.randint(20,50)
   t.forward(l)
   t.forward(-l)
   t.right(12)

for i in range(10):
  turtle.colormode(255)
  x=random.randint(-200,200)
  y=random.randint(-200,200)
  clr=random.randint(0,255),random.randint(0,255),random.randint(0,255)
  firework(x,y,clr)
s.mainloop() 
