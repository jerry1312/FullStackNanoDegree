import turtle

window=turtle.Screen()

window.bgcolor("gray")

brad=turtle.Turtle()
brad.speed(0)

def square():
	for i in range(0,4,1):
		brad.forward(100)
		brad.left(90)

for i in range(1,100,1):
	square()
	brad.left(10)


window.exitonclick()
