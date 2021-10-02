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
import random
import time

print(coffee)
print("本日、コーヒーを奢るのは誰だ？")

name = input("参加者の名前を入力してください。Ex) 田中, 鈴木 >>>   ").split()

print(f"合計 {len(name)}名が参加しました。")

winner = random.choice(name)

print("今日選ばれた人は。。")
time.sleep(5)
print(f"{winner}様です。")