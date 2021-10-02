#英語単語検索プログラム

dict_eng = {"apple" : "リンゴ", "peach" : "モモ", "banana" : "バナナ"}

user_input = input("検索する英単語を入力してください >>>> ")

if user_input in dict_eng:
    print(f"検索した{user_input}の意味は{dict_eng[user_input]}です。")
else:
    print("検索した単語は登録されてません。")