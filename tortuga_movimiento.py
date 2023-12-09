import turtle as t

tortuga =t.Screen()
t.speed('fastest')
grados=0


#tortuga = turtle.Turtle()


def RI():
    global grados
    if (grados == 0):
        t.setheading(grados)
        t.forward(10)
    else:
        grados=0
        t.setheading(grados)
        t.forward(10)


def LI():
    global grados
    if (grados == 180):
        t.setheading(grados)
        t.forward(10)
    else:
        grados=180
        t.setheading(grados)
        t.forward(10)


def UP():
    global grados
    if (grados == 90):
        t.setheading(grados)
        t.forward(10)
    else:
        grados=90
        t.setheading(grados)
        t.forward(10)


def DO():
    global grados
    if (grados == 270):
        t.setheading(grados)
        t.forward(10)
    else:
        grados=270
        t.setheading(grados)
        t.forward(10)


tortuga.onkey(LI,"a")
tortuga.onkey(RI,"d")
tortuga.onkey(UP,"w")
tortuga.onkey(DO,"s")
tortuga.listen()
t.done()
