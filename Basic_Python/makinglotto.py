import random

lotto_num = [] #番目ロト番号リスト生成

def getRandomNum():
    num = random.randint(1,43)
    return num

count = 0

#無限繰り返し
while True:
    if count > 5:
        break
    random_num = getRandomNum() #ランダムで１つの数字を選択
    if random_num not in lotto_num: #各数字が被らないようにする
        lotto_num.append(random_num)
        count = count + 1