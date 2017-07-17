import turtle

window=turtle.Screen()

window.bgcolor("gray")


brad=turtle.Turtle()
brad.speed(0)
brad.color("cyan")
brad.shape("turtle")
def square():
	for i in range(0,4,1):
		brad.circle(100,60)
		brad.left(120)
def circle():
	brad.circle(120)

for i in range(1,13,1):
	square()
	brad.left(30)
brad.right(90)
brad.forward(250)

window.exitonclick()
