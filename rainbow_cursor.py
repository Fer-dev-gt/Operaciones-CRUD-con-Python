import turtle

window = turtle.Screen()

colors = ['red','purple','blue','green','yellow','orange']

tortuga = turtle.Pen()
tortuga.speed(0)

for i in range(360):
	tortuga.pencolor(colors[i%6])
	tortuga.width(i/100+1)
	tortuga.forward(i)
	tortuga.left(59)

window.mainloop()
