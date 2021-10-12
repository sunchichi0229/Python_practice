import turtle as t
import random

def turn_left():
    player.left(30)

def turn_right():
    player.right(30)

def rand_pos():
    x_cor = random.randint(-250, 250)
    y_cor = random.randint(-250, 250)
    return x_cor, y_cor

#環境設定
t.setup(600, 600)
t.bgcolor("skyblue")
t.up()
t.ht()

#変数
player_speed = 5
score = 0
game_over = False

#点数の表示
t.goto(0, 250)
t.write(f"score : {score}", False, "center", ("", 20))

#プレイヤー
player = t.Turtle()
player.shape("turtle")
player.shapesize(2)
player.up()
player.color("lavender")
player.speed(0)

#餌
food = t.Turtle()
food.ht()
food.shape("triangle")
food.up()
food.color("darkgreen")
food.speed(0)
food.setheading(90)
food.goto(rand_pos())
food.st()

#毒入り餌
p_food = t.Turtle()
p_food.ht()
p_food.shape("triangle")
p_food.up()
p_food.color("red")
p_food.speed(0)
p_food.setheading(90)
p_food.goto(rand_pos())
p_food.st()


t.onkeypress(turn_left, "Left")
t.onkeypress(turn_right, "Right")
t.listen()

while not game_over:
    player.forward(player_speed)

    if player.xcor() > 260 or player.xcor() < -260 or player.ycor() > 260 or player.ycor() < -260:
        player.right(180)

    if player.distance(food) < 20:
        food.goto(rand_pos())
        p_food.goto(rand_pos())
        player.speed += 1
        score += 1
        t.clear()
        t.write(f"score : {score}", False, "center", ("", 20))

    if player.distance(p_food) < 20:
        game_over = True

t.goto(0,0)
t.write("Game Over", False, "center", ("", 50))

t.done()