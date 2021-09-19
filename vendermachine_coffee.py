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

else:
    print("金額が足りないです。注文が取り消されました。")
