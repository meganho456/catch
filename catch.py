import turtle
import time

# screen
sc = turtle.Screen()
sc.title("game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)

# initialize score
player = 0

# score display at top of screen
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("black")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Player Score: 0", align="center", font=("Arial", 20, "normal"))

# paddle
pad = turtle.Turtle()
pad.speed(0)
pad.shape("square")
pad.color("black")
pad.shapesize(stretch_wid=2, stretch_len=6)
pad.penup()
pad.goto(0, -240)

# ball
hit_ball = turtle.Turtle()
hit_ball.speed(70)
hit_ball.shape("circle")
hit_ball.color("black")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -6

# move paddle left and right
def paddleright():
	x = pad.xcor()
	x += 20
	pad.setx(x)

def paddleleft():
	x = pad.xcor()
	x -= 20
	pad.setx(x)

# set keys to move paddle
sc.listen()
sc.onkeypress(paddleright, "Right")
sc.onkeypress(paddleleft, "Left")

while True:

	sc.update()

	hit_ball.setx(hit_ball.xcor()+hit_ball.dx)
	hit_ball.sety(hit_ball.ycor()+hit_ball.dy)

	# making ball bounce off borders of screen
	if hit_ball.xcor() > 470:
		hit_ball.setx(470)
		hit_ball.dx *= -1

	if hit_ball.xcor() < -470:
		hit_ball.setx(-470)
		hit_ball.dx *= -1

	if hit_ball.ycor() > 280:
		hit_ball.sety(280)
		hit_ball.dy *= -1

	if hit_ball.ycor() < -300:
		sketch.clear()
		sketch.write("Your score is {}.".format(player), align="center", font=("Arial", 20, "normal"))
		time.sleep(2)
		hit_ball.goto(0, 0)
		# resetting speed
		hit_ball.dy = -6
		player = 0
		sketch.clear()
		sketch.write("Player Score: {}".format(player), align="center", font=("Arial", 20, "normal"))

	# making ball bounce off paddle and adding 1 to player score
	if (hit_ball.ycor()<-200 and hit_ball.ycor()>-210) and (hit_ball.xcor()<pad.xcor()+40 and hit_ball.xcor()>pad.xcor()-40):
		hit_ball.sety(-200)
		# increase speed every time ball bounces off
		hit_ball.dy *= -1.2
		player +=1
		sketch.clear()
		sketch.write("Player Score: {}".format(player), align="center", font=("Arial", 20, "normal"))