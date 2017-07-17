import turtle

window=turtle.Screen()

window.bgcolor("gray")


brad=turtle.Turtle()
brad.speed(0)
brad.color("cyan")
brad.shape("turtle")
def square():
	for i in range(0,4,1):
		brad.forward(100)
		brad.left(90)
def circle():
	brad.circle(120)

for i in range(1,100,1):
	square()
	circle()
	brad.left(10)


window.exitonclick()
