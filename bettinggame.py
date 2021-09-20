door = """
*************       *************        *************
*           *       *           *        *           *
*   doorA   *       *   doorB   *        *   doorC   *
*     1     *       *     2     *        *     3     *
*************       *************        *************

"""

road = """
     A            A         B            B        C         C
      A            A         B          B        C          C
        A           A         B         B      C           C
          A      1   A        B     2  B      C      3    C
            A         A      B         B      C          C
             A          A   B         B     C           C
              A         A B          B     C          C
                A       AB            B  C          C
                 A      AB             BC          C


"""

import random

print("ようこそ！このゲームへ")
print("一つのレベルをクリアするたび、賭けた金額の２倍を賞金としてもらえます。")
print("レベルクリアに失敗した場合、すべての金額を失います。")
print("="*50)

bet = int(input("賭ける金額を入力してください。単位:$ >>>  "))
print(f"合計${bet}を賭けました。")

print(road)
winning_num = random.randint(1,3)

user_choice = int(input("道が３つに分かれています。どの道を選択しますか？1,2,3 >>> "))

if user_choice == winning_num:
    print(f"おめでとうございます。２倍獲得。合計金額は${bet * 2}になりました。")
    next_level = input("次の段階に移動しますか？勝ったら２倍、負けたら$０。y or n >>>").lower()
    if next_level == 'y':
        print("次の段階に移動。")
        print(door)
        winning_num = random.randint(1,3)
        print(winning_num)
        user_choice = int(input("３つのドーアがあります。どのドーアを選択しますか？1,2,3 >>> "))
        if winning_num == user_choice:
            print(f"おめでとうございます。合計金額は${bet * 4}になりました。")
        else:
            print("すべての金額を失われました。")
    else:
        print(f"ゲームが終了。合計金額は${bet * 2}になりました。")
else:
    print("すべての金額を失われました。")