import turtle as t

t.bgcolor("black")
t.speed(0)
t.pensize(2)

colors = ['orange', 'orange', 'orange', 'orange', 'white','white','white','white', 'green', 'green','green', 'green']

a=0

for i in range(144):
    t.color(colors[i%12])
    for i in range(12):
        t.circle(10,180)
        t.left(180)
        t.circle(10,-180)
        t.left(180)
    t.penup()
    t.setpos(0,0)
    t.pendown()
    a+=10
    t.seth(a)
t.hideturtle()
