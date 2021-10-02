import turtle as t
import random

color = ("red", "orange", "blue", "green", "white")

t.bgcolor("black")

t.speed(0)
for x in range(20):
    t.up()
    t.goto(random.randint(-300,300), random.randint(-300,300))
    t.down
    #星を描く
    t.color(random.choice(color))
    t.begin_fill()
    star_size = random.randint(10,30)
    for i in range(5):
        t.forward(star_size)
        t.left(144)
    t.end_fill()
t.done()