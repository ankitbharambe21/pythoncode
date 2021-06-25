import turtle
import math

b = turtle.Turtle()
b.speed(600)

window = turtle.Screen()
window.bgcolor("black")
b.pencolor("yellow")
b.pensize(1)

ankit = 50

b.left(90)
b.penup()
b.goto(-7 * ankit, 0)
b.pendown()

for a in range(-7 * ankit, -3 * ankit, 1):
    x = a / ankit
    rel = math.fabs(x)
    y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
                1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                        math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
    b.goto(a, y * ankit)

for a in range(-3 * ankit, -1 * ankit - 1, 1):
    x = a / ankit
    rel = math.fabs(x)
    y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
        math.fabs(rel - 1) / (rel - 1))
    b.goto(a, y * ankit)

b.goto(-1 * ankit, 3 * ankit)
b.goto(int(-0.5 * ankit), int(2.2 * ankit))
b.goto(int(0.5 * ankit), int(2.2 * ankit))
b.goto(1 * ankit, 3 * ankit)

for a in range(1 * ankit + 1, 3 * ankit + 1, 1):
    x = a / ankit
    rel = math.fabs(x)
    y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
        math.fabs(rel - 1) / (rel - 1))
    b.goto(a, y * ankit)

for a in range(3 * ankit + 1, 7 * ankit + 1, 1):
    x = a / ankit
    rel = math.fabs(x)
    y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
                1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                        math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
    b.goto(a, y * ankit)

for a in range(7 * ankit, 4 * ankit, -1):
    x = a / ankit
    rel = math.fabs(x)
    y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
    b.goto(a, y * ankit)

for a in range(4 * ankit, -4 * ankit, -1):
    x = a / ankit
    rel = math.fabs(x)
    y = math.fabs(x / 2) - 0.0913722 * x ** 2 - 3 + math.sqrt(1 - (math.fabs(rel - 2) - 1) ** 2)
    b.goto(a, y * ankit)

for a in range(-4 * ankit - 1, -7 * ankit - 1, -1):
    x = a / ankit
    rel = math.fabs(x)
    y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
    b.goto(a, y * ankit)

b.penup()
#b.goto(600, 600)
b.goto(-160,160)
b.write("    Batman", font=("Arial",40,"bold"),align =("left"))

b.goto(-300,-300)
style = ("Arial",40,"bold")
b.write("       By - ankit_coding", font=style, align='left')
b.hideturtle()
turtle.done()
