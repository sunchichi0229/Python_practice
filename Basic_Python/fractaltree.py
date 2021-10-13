import turtle as t
import random

def tree(length, pen_size):
    angle = random.randint(15, 30)
    branch = random.uniform(0.6, 0.9)
    r_color = random.choice(color_list)

    if length < 35:
        t.color(r_color)
        t.stamp ()
        t.color("brown")

    if length > 12:
        t.pensize(pen_size)
        pen_size *= 0.7
        t.forward(length)
        t.left(angle)      #左枝書く
        tree(length * branch, pen_size)
        t.right(angle * 2)    #右枝書く
        tree(length * branch, pen_size)
        t.left(angle)
        t.backward(length)

def grass():
    t.up()
    t.goto(-380, -280)
    t.shapesize(7)
    while t.xcor() < 380:
        t.setheading(0)
        t.forward(15)
        t.color(random.choice(color_list))
        t.setheading(random.randint(60, 120))
        t.stamp()

color_list = ["green", "darkgreen", "greenyellow", "forestgreen", "yellowgreen"]

t.bgcolor("lightblue")
t.setheading(90)
t.speed(0)
t.up()
t.goto(0, -300)
t.down()
t.color("brown")
tree(100, 10)
grass()


t.done()