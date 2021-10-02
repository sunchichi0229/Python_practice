#1から100まで合計

sum_100 = 0

for i in range(1,101):
    sum_100 += i

print(f"1から100まで合計 : {sum_100}")

#1から100まで偶数の合計

sum_even = 0

for i in range(2,101,2):
    sum_even += i

print(f"1から100まで偶数の合計 : {sum_even}")