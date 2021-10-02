juice_art = """

                |       @   @ |
                |   @     @   |
                |  @   @      |
                |  @    @     |   
                |   @        @|
                |           @ |
                ---------------    
"""

print(juice_art)
print("== フジカフェ管理者モード ==")

flavor = ["リンゴ","マンゴ","バナナ"]

print(" ==== メニュー ====")
for i in flavor:
    print(f"{i}ジュース")

user_input = 0
while user_input != '5':

    print("""
    ==== 管理者モード ====
    1. メニュー閲覧
    2. 新メニュー追加
    3. メニュー削除
    4. メニュー名前変更
    5. 管理者モード終了
    ======================
    """)

    user_input = input("機能を選択してください >>> ")

    if user_input == '1':
        print(" ==== メニュー ====")
        for i in flavor:
            print(f"{i}ジュース")
    elif user_input == '2':
        new_flaver = input("新たなメニューを入力してください >>> ")
        flavor.append(new_flaver)
    elif user_input == '3':
        remove_flaver = input("削除したいメニューを入力してください")
        flavor.remove(remove_flaver)
    elif user_input == '4':
        for i in range(len(flavor)):
            print(f"{i}. {flavor[i]}")

        index = int(input("何番目のメニューを変更しますか？>>> "))
        new_name = input("変更する名前を入力してください >>> ")

        print(f"{flavor[index]}メニューを{new_name}に変更します。")
        flavor[index] = new_name
        