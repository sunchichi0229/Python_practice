import turtle as t
import time
import random

t.bgcolor("pink")
t.ht()
t.up()

num_times = int(t.textinput("覚えよNumberゲーム", "何個の数字を利用しますか？"))

t.write("覚えよNumberゲームを始めます。", False, "center", ("", 30))
time.sleep(3)
t.clear()

num = ""
for x in range(num_times):
    rand_num = random.randint(1, 50)
    t.write(rand_num, False, "center", ("", 70))
    num += str(rand_num)
    num += " "
    time.sleep(1)
    t.clear()

user_input = t.textinput("覚えよNumberゲーム", "覚えた数字を入力してください")

if user_input == num.strip():
    t.write("正解", False, "center", ("", 30))
else:
    t.write("外れ", False, "center", ("", 30))
    t.goto(0, -50)
    t.write(f"正解は {num}です", False, "center", ("", 30))
    t.goto(0, -100)
    t.write(f"入力した数字は {user_input}です", False, "center", ("", 30))




t.done()