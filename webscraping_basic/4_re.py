import re

p = re.compile("ca.e")
# .(ca.e): １つの文字を意味 > care, cafe, case...等 | caffe (x)
# ^(^de): 文字列の始め > desk, destination | fade(x)
# $(se$): 文字列の最後 > case, base | face(x).

def print_match(m):
    if m:
        print("m.group():", m.group()) #一致する文字列を返す
        print("m.string():", m.string()) #入力してもらった文字列を返す
        print("m.start():", m.start()) #一致する文字列の始め index
        print("m.start()", m.end()) #一致する文字列の最後 index
        print("m.span()", m.span()) #一致する文字列の最初/最後　index
    else:
        print("マッチしてない")

m = p.match("careless") # match : 与えられた文字列が最初から一致するか確認 
print_match(m)

m = p.search("good care") # search : 与えられた文字列の中に一致するものがあるか確認
print_match(m)

lst = p.findall("careless") #findall : 一致する全ての値をリスト形態に返す
print(lst)


# 正規式を表す方法
# 1. p = re.compile("自分で決める形態")
# 2. m = p.match("比べる文字列") : 与えられた文字列が最初から一致するか確認 
# 3. m = p.search("比べる文字列") : 与えられた文字列の中に一致するものがあるか確認
# 4. lst = p.findall("比べる文字列") :  一致する全ての値をリスト形態に返す

# 自分で決める形態 : 正規式
# .(ca.e): １つの文字を意味 > care, cafe, case...等 | caffe (x)
# ^(^de): 文字列の始め > desk, destination | fade(x)
# $(se$): 文字列の最後 > case, base | face(x).