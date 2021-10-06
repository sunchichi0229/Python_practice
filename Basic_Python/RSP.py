import turtle as t
import random

def com_choice():
    rand_choice = random.randint(0, 2)
    com.shape(images[rand_choice])
    return com_list[rand_choice]

def result_print(user_c, com_c):
    global user_score, com_score
    t.clear()
    t.goto(0, -100)
    if user_c == com_c:
        t.write("引分", False, "center", ("", 50))
    elif winning_case[user_c] == com_c:
        user_score += 1
        user_pen.clear()
        user_pen.write(user_score, False, "center", ("", 50))
        t.write("勝", False, "center", ("", 50))
    else:
        com_score += 1
        com_pen.clear()
        com_pen.write(com_score, False, "center", ("", 50))
        t.write("負", False, "center", ("", 50))

def rock(x, y):
    user.shape(rock_gif)
    com = com_choice()
    result_print("rock", com) #勝負の結果判定

def scissors(x, y):
    user.shape(scissors_gif)
    com = com_choice()
    result_print("scissors", com) #勝負の結果判定

def paper(x, y):
    user.shape(paper_gif)
    com = com_choice()
    result_print("paper", com) #勝負の結果判定

#基本設定
t.bgcolor("lavender")
t.title("じゃんけんゲーム")
t.ht()
t.up()

rock_gif = "C:/Users/sumyo/Python_practice/Basic_Python/imgs/rock.gif"
scissors_gif = "C:/Users/sumyo/Python_practice/Basic_Python/imgs/scissors.gif"
paper_gif = "C:/Users/sumyo/Python_practice/Basic_Python/imgs/paper.gif"
t.addshape(rock_gif)
t.addshape(scissors_gif)
t.addshape(paper_gif)

images = [rock_gif, scissors_gif, paper_gif ]
com_list = ["rock", "scissors", "paper"]
winning_case = {"rock" : "scissors", "scissors" : "paper", "paper" : "rock"}
user_score = 0
com_score = 0

#自分の選択イメージ
user = t.Turtle()
user.up()
user.speed(0)
user.goto(-200, 200)
user.write("自分の選択", False, "center", ("", 30))
user.goto(-200, -100)
user.shape(rock_gif)

#COMの選択イメージ
com = t.Turtle()
com.up()
com.speed(0)
com.goto(200, 200)
com.write("相手の選択", False, "center", ("", 30))
com.goto(200, -100)
com.shape(rock_gif)

#ユーザー点数ペン
user_pen = t.Turtle()
user_pen.ht()
user_pen.up()
user_pen.goto(-200, 100)
user_pen.write(user_score, False, "center", ("", 50))

#COM点数ペン
com_pen = t.Turtle()
com_pen.ht()
com_pen.up()
com_pen.goto(200, 100)
com_pen.write(com_score, False, "center", ("", 50))

t.onscreenclick(rock, 1) #Mouse 左
t.onscreenclick(scissors, 2) #Mouse wheel
t.onscreenclick(paper, 3) #Mouse 右


t.done()