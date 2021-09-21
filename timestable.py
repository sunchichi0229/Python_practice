multi_art = """
            k                                                 s s           
        kkkkkkkkkkk             k                     s    s           n  
            k     k            kkkkkkkkkk           sssssssssss          n  
            k     k           k     k                 s    s                  n
            k     k                 k                      s               n 
            k     k                 k                      s            n 

"""

print("!!掛け算出力プログラム")
print(multi_art)

app_off = "いいえ"
while app_off == "いいえ":
    num = int( input("掛け算。。何段を出力しますか？>>>   "))

    for i in range(1,10):
        print(f"{num} x {i} = {num*i}")  

    app_off = input("プログラムを終了しますか？はい/いいえ　>>>   ")
    print("="*50)

print("プログラムが終了しました。")