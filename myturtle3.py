import turtle 
#mt = turtle.Turtle()   # Screen popup
mt = turtle.Pen()
mt.shape("turtle")
mt.color("red","green")  # color fill 1 , 2
mt.begin_fill()
for i in range(4):
    mt.forward(100)
    mt.left(90)
mt.end_fill()
mt.penup()
mt.right(90)
mt.forward(20)
mt.pendown()
mt.color("red","yellow")
mt.begin_fill()
for i in range(4):
    mt.forward(100)
    mt.left(90)
mt.end_fill()
mt.penup()  # # Pen UpWard
mt.forward(40)
mt.right(90)
mt.forward(20)
mt.pendown()  # Pen DownWard
mt.color("red","pink")  # color fill 1 , 2
mt.begin_fill()
for i in range(4):
    mt.forward(100)
    mt.right(90)
mt.end_fill()
def Go(x,y):
    mt.penup()  # Pen UpWard
    mt.goto(x,y)
    mt.pendown() # Pen DownWard
Go(-20,-120)
turtle.done()  # Frame still shown after finished Loop 
