import turtle
d=turtle.Turtle() #pen
s=turtle.Screen() #paper
s.bgcolor("sky blue")
d.speed(10)

def makeSquare(clr,size):
   turtle.fillcolor(clr)
   d.color(clr) 
   d.begin_fill()
   d.begin_fill()
   for i in range(4):
      d.forward(size)
      d.right(90)
   d.end_fill()
   
def reposition(x,y):
    d.penup()
    d.goto(x,y)
    d.pendown() 

def makeRectangle(clr,size1,size2):
    d.color(clr)
    d.begin_fill()
    for i in range(2):
      d.forward(size1)
      d.right(90)
      d.forward(size2)
      d.right(90)
    d.end_fill() 

def makeTriangle(clr,size):
    d.color(clr)
    d.begin_fill()
    for i in range(3):
      d.forward(size)
      d.left(120)
    d.end_fill()

#sun
reposition(100,100)              
makeSquare("yellow",50)
reposition(90,75)       
d.left(45)
makeSquare("yellow",50)
d.right(45)

#ground
reposition(-350,-100)
makeRectangle("gold",600,70)

#pyramid
reposition(-90,-100)
makeTriangle("goldenrod",100)

#Stripes
d.width(3)
d.color("black")
reposition(-85,-90)
d.forward(90)
d.width(3)
d.color("black")
reposition(-77,-80)
d.forward(77)
d.color("black")
reposition(-71,-70)
d.forward(64)
d.color("black")
reposition(-67,-60)
d.forward(53)
d.color("black")
reposition(-77,-80)
d.forward(77)
d.color("black")
reposition(-77,-80)

#Mountain
d.color("brown")
reposition(100,-100)
d.left(90)
d.begin_fill()
d.fillcolor("brown")
for i in range(19):
 d.forward(5)
 d.right(10)
d.end_fill()

#Cactus
d.color("green")
d.setheading(90)
reposition(115,-70)
d.begin_fill()
d.fillcolor("green")
d.forward(30)
d.left(90)
for i in range(18):
   d.forward(2)
   d.right(10)
d.left(90)
for i in range(19):
   d.forward(2)
   d.right(10)
d.forward(5)
d.left(90)
for i in range(18):
   d.forward(2)
   d.right(10)
d.left(90)
d.forward(22)
d.end_fill()

s.mainloop()

