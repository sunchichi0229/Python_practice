import turtle as t
import random

def rock(x, y):
    user.shape(rock_gif)
    #COMの選択 - ランダム選択
    #勝負の結果判定

def scissors(x, y):
    user.shape(scissors_gif)
    #COMの選択 - ランダム選択
    #勝負の結果判定

def paper(x, y):
    user.shape(paper_gif)
    #COMの選択 - ランダム選択
    #勝負の結果判定

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

t.onscreenClick(rock, 1) #Mouse 左
t.onscreenClick(scissors, 2) #Mouse wheel
t.onscreenClick(paper, 3) #Mouse 右


t.done()