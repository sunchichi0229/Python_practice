import turtle as t
import random

t.speed(0)
def petal(size, angle):
    for i in range(2):
        t.circle(size, angle)
        t.left(180 - angle)

def draw_flower(petal_num, petal_size, petal_angle):
    t.color("pink")
    t.begin_fill()
    for i in range(petal_num):
        petal( petal_size, petal_angle)
        t.left(360/petal_num)
    t.end_fill()

    t.goto(0, -30)
    t.ht()
    t.color("yellow")
    t.begin_fill()
    t.circle(30)
    t.end_fill()

t.bgcolor("ivory")
petal_num = random.randint(4, 10)
petal_size = random.randint(50, 120)
petal_angle = random.randint(90, 130)

draw_flower(petal_num, petal_size, petal_angle)



t.done()