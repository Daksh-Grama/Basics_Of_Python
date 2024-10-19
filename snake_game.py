import turtle, random, time

s = turtle.Screen()
snake = turtle.Turtle()

s.bgcolor("black")
snake.color("green")
snake.shape("square")

snake.penup()
snake.direction = "stop"

score = 0
segment = []

def movesnake():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y+5)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y-5)


    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x-5)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x+5)


def go_up():
    snake.direction = "up"

def go_down():
    snake.direction = "down"

def go_right():
    snake.direction = "right"

def go_left():
    snake.direction = "left"


s.listen()
s.onkey(go_up, "Up")
s.onkey(go_down, "Down")
s.onkey(go_right, "Right" )
s.onkey(go_left, "Left" )

Food = turtle.Turtle()
Food.shape("circle")
Food.color("red")
Food.penup()
Food.goto(100,100)

pen = turtle.Turtle()
pen.hideturtle()

while True :
    s.update()
    movesnake()
    time.sleep(0.1)

    if snake.distance(Food) < 20 :
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        Food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.shape("square")

        c = ["blue", "green", "purple", "yellow", "pink", "white"]
        color1 = random.choice(c)
        new_segment.color(color1)
        new_segment.penup()
        segment.append(new_segment)
        pen.color("white")
        score = score + 1
        pen.clear()
        pen.write("SCORE = {}".format(score),
                  align="center",
                  font=("Arial", 20, "bold"))

        # if score > highscore:
        #     highscore = score
        #     pen2.color("blue")
        #     pen2.goto(0, 30)
            #pen2.write("HIGHSCORE = {}".format(score) ,align="center",font=("Arial",30,"bold"))

    for i in range(len(segment) - 1, 0, -1):
        x = segment[i - 1].xcor()
        y = segment[i - 1].ycor()
        segment[i].goto(x, y)

    if len(segment) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segment[0].goto(x, y)







    


    

 