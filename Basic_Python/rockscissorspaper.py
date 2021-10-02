rock = """
        *****
        *****
        *****
"""

scissors = """
        *     *
         *   *
          ***
"""

paper = """
        *  *   *   *
        *  *   *   *
        *  *   *   *
        ************
"""

import random

game_option = [rock, scissors, paper]
com_choice = random.randint(0,2)

user_choice = int(input("0: グー, 1: チョキ, 2: パ >>> "))

print("私の選択: ")
print(game_option[user_choice])

print("コンピューターの選択: ")
print(game_option[com_choice])

if com_choice == user_choice:
    print("引き分けです。")
elif user_choice - com_choice == -1 or (user_choice == 2 and com_choice == 0):
    print("勝ちました。")
else:
    print("負けました。")