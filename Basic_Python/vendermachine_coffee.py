coffee = """
        S       S        S
        S       S       S
       S         S       S 
        S         S     S     
     ************************      ***
      **                  **      ***          
       **    *Coffee*    **     ****            
        **              **   ****           
           ************ 
"""

menu = """
            藤村自販機
            - M E N U -
        
        1 : ブラックコーヒー　　180円
        2 : 抹茶フラペチーノ    570円
        3 : カフェラッテ        230円 

"""
print(coffee)
print(menu)
print('='*45)

coffee_price = 0 #コーヒー一杯分の金額
total_price = 0 #注文したコーヒーの合計金額
change = 0 # 釣銭

order = int(input("飲み物の種類を選んでください。番号入力 >>>>>>>>"))

if order == 1:
    coffee_price = 180
elif order == 2:
    coffee_price = 570
elif order == 3:
    coffee_price = 230

cups = int(input("何個注文しますか？数入力 >>>>>>>>"))
total_price = coffee_price * cups

received = int(input(f"合計　{total_price}円です。お金を入れてください"))
if received >= total_price:
    change = received - total_price
    print(f"{received}円を受け取りました。釣銭は{change}です。")
    # 1000円、500円、100円、50円、10円 Ex) 1970円 => 1000円：１枚、500円:1個、100円:4個、50円:1個、10円:2個
    # 2360円があると仮定します。
    # 1000円 => 2360//1000  100円 => 360//100

    change_1000 = change // 1000
    remain_1000 = change % 1000
    change_500 = remain_1000 // 500
    remain_500 = change_500 % 500
    change_100 = remain_500 // 100
    remain_100 = change_100 % 100
    change_50 = remain_100 // 50
    remain_50 = change_50 % 50
    change_10 = remain_50 // 10
    remain_10 = change_10 % 10

    print(f"1000円{change_1000}枚、500円{change_500}個、100円{change_100}個、50円{change_50}個、10円{change_10}個です。")

else:
    print("金額が足りないです。注文が取り消されました。")
