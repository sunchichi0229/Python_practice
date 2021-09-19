food_icon = """
    ****** 
    ******
    ******
"""

menu ="""
        -メーニュー-

        お好み焼き: 1200円
        たこ焼き: 800円
        チチミ: 1000円

        セット注文: 300円追加
        (セットは飲み物が追加されます。)
"""

print(food_icon)
print("藤村家にようこそ")
print("="*50)
print(menu)
print("="*50)
print()

order = input("メーニューを選んでください。(お好み焼き、たこ焼き、チチミ)")
combo = input("セット注文しますか?(その場合、300円追加) ex>　はい / いいえ")

price = 0

if order == 'お好み焼き':
    price = 1_200
elif order == 'たこ焼き':
    price = 800
else:
    price = 1_000

if combo == 'はい':
    price += 300

print(f"合計は{price}円です。")