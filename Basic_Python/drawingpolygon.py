import turtle

turtle.shape("turtle") #triangle / square / arrow / circle
turtle.bgcolor("pink")
turtle.pensize("10")

polygon = int( turtle.numinput("多角形", "何角形を描きましょうか？"))

for i in range(polygon):
    turtle.forward(100)
    turtle.left(360/polygon)




turtle.done()