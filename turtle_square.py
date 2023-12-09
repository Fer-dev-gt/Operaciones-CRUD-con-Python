import turtle

turtle.shape("turtle")
tortuga = turtle.color("red")

window = turtle.Screen()


for i in range (1, 100):
	turtle.forward(i*2)
	turtle.right(90)

turtle.done()
window.mainloop()

