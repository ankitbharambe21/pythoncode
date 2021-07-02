import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("JAI BAJRANGBALI")

t = turtle.Turtle()
t.pencolor("white")
t.speed(9)
t.width(4)
t.pencolor("orange")
t.hideturtle()
#define curve
def curve():
    for i in range(60):
        t.left(3)
        t.forward(1)
# define eyebrow
def curveyebrow():
    for i in range(30):
        t.forward(6)
        t.right(2)
#define nose
def curvenose():
    for i in range(15):
        t.forward(1)
        t.right(1)

def curvenosepoint1():
    for i in range(10):
        t.forward(2)
        t.right(1)

def curvenosepoint2():
    for i in range(5):
        t.forward(2)
        t.right(1)

def belownoseline1():
    for i in range(8):
        t.forward(6)
        t.left(5)

def belownoseline2():
    for i in range(8):
        t.forward(5)
        t.right(5)
#define lips
def upperlip():
    for i in range(10):
        t.forward(10)
        t.left(10)
    for x in range(10):
        t.forward(3)
        t.right(10)

def lowerlip():
    for i in range(10):
        t.forward(6)
        t.right(6)
 #define chin       
def chincurve():
    for i in range(15):
        t.forward(12)
        t.left(6)
#define eye
def eye():
    for i in range(10):
        t.forward(8)
        t.right(4)
    for a in range(10):
        t.forward(2)
        t.left(7)

t.penup()
t.goto(-100,250)
t.pendown()

t.right(80)
t.forward(70)
curve()
t.forward(70)
t.backward(70)
t.penup()
t.left(90)
t.width(10)
t.forward(20)
t.pendown()
t.pencolor("white")
t.right(90)
t.forward(60)
t.backward(60)
t.penup()
t.right(90)
t.forward(40)
t.pendown()
t.pencolor("orange")

t.width(15)
t.left(30)
t.forward(10)
curveyebrow()

t.right(140)
t.penup()
t.forward(230)
t.width(8)
t.forward(10)
t.left(79)
t.forward(10)
t.pendown()
t.left(90)
t.width(10)
t.right(80)
t.forward(20)
t.right(25)
t.width(10)
t.forward(70)
t.left(60)
t.forward(30)
curvenose()
t.width(5)
t.left(60)

t.penup()
t.forward(20)
t.left(80)
t.forward(5)
t.pendown()
t.width(8)
t.forward(5)
t.right(45)
t.width(8)
t.forward(5)
curvenosepoint1()

t.penup()
t.forward(15)
t.pendown()
t.width(10)
t.right(120)
t.forward(15)
t.right(40)
t.forward(20)
t.right(20)
t.forward(10)
curvenosepoint2()

t.penup()
t.right(30)
t.forward(30)
t.left(100)
t.forward(15)
t.pendown()
t.width(5)
t.forward(5)
belownoseline1()

t.penup()
t.left(70)
t.forward(15)
t.left(90)
t.pendown()
t.width(5)
t.forward(10)
belownoseline2()

t.penup()
t.backward(45)
t.right(110)
t.forward(30)
t.pendown()
t.width(10)
t.forward(5)
upperlip()

t.penup()
t.right(100)
t.forward(70)
t.pendown()
t.right(30)
t.forward(15)
lowerlip()

t.penup()
t.backward(23)
t.left(150)
t.pendown()
t.forward(10)
chincurve()

t.penup()
t.left(100)
t.forward(350)
t.pendown()
t.right(90)
t.forward(15)
eye()

t.penup()
t.backward(50)
t.left(90)
t.forward(40)
t.dot(30, "red")
t.dot(10, "black")
t.goto(-338,-350)
style = ("Bradley Hand ITC",40,"bold")
t.write("            BY - @ankit_coding", font=style, align='left')
turtle.done()
