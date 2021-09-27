import random

eng_word = [["orbit", "軌道"], ["gravity", "重力"], 
            ["laboratory", "実験室"], ["oxygen", "酸素"],
            ["nutrient", "栄養素"], ["satellite", "衛星"],
            ["galaxy", "銀河"],  ["germ", "未生物"],  
            ["planet", "星"], ["ethics", "倫理"], 
            ["culture shock", "カルチャーショック"], ["ad", "広告"]
            ]

quiz_on = True
score = 0
quiz_num = 0

while quiz_on:
    #4択項目作成
    quiz_num += 1
    multi_choice = random.sample(eng_word, 4)
    answer_index = random.randint(0, 3) #0, 1, 2, 3

    print(f"問題{quiz_num}. {multi_choice[answer_index][0]}の意味は？")

    #例文を出力
    for i in range(4):
        print(f"{i+1}. {multi_choice[i][1]}")

    print()
    user_input = int(input("答えを入力してください。終了: 0 >>>> "))

    if user_input == 0:
        quiz_on = False
        print("Quizが終了しました。")
        print(f"合計{quiz_num-1}問題の中で{score}問題を当てました。")
    elif user_input == answer_index + 1:
        score += 1
        print("正解です。")
    else:
        print(f"間違いました。正解は{answer_index + 1}です。")
    print()