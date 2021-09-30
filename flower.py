import turtle as t

t.speed(0)
def petal():
    for i in range(2):
        t.circle(150, 110)
        t.left(70)

def draw_flower():
    t.color("pink")
    t.begin_fill()
    for i in range(5):
        petal()
        t.left(360/5)
    t.end_fill()

    t.goto(0, -30)
    t.ht()
    t.color("yellow")
    t.begin_fill()
    t.circle(30)
    t.end_fill()

t.bgcolor("ivory")
draw_flower()



t.done()