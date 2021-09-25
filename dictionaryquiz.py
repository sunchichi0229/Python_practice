dict_eng = {"apple" : "リンゴ", "peach" : "モモ", "banana" : "バナナ",
             "mango" : "マンゴ", "spring" : "春", "winter" : "冬"}

for i in dict_eng:
    user_input = input(f"{i}の意味は? >>>> ")

    if user_input == dict_eng[i]:
        print("正解です。")
    else:
        print(f"間違いました。正解は{dict_eng[i]}です。")