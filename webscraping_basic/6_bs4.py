import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/#/"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soupオブジェクトから始めて発見されるElementを出力
# print(soup.a.attrs)　# a elementのオブジェクト情報を出力
# print(soup.a["href"]) # a elementのhrefオブジェクトの値を出力

# soup.find("a", attrs={"class":"Nbtn_upload"}) # aの中にあるclass="Nbtn_upload"を探してくれという意味

# print(soup.find("div", attrs={"class":"wbus122"}))

# rank1 = soup.find("tr", attrs={"class":"RankingTable_tr__2nw3W"})
# print(rank1.a.get_text())
# print(rank1.next_sibling) #siblingは次の順番に行かせるもの
# print(rank1.next_sibling.next_sibling) #１回で出てこない場合は2回入力する

# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling

# print(rank3.div.get_text())
# rank2 = rank3.previous_sibling.previous_sibling #以前の値に移る場合はprevious

# print(rank1.parent) #親オブジェクトが出力される

# rank2 = rank1.find_next_sibling("tr") #この場合は自分が探したいtagの値を探せる入力値
# print(rank2.div.get_text())


# rank1 = rank2.find_previous_sibling("tr") #この場合は自分が探したいtagの値を探せる入力値
# print(rank2.div.get_text())

# rank1.find_next_siblings("tr") #siblingの後ろにsをつけることですべての情報を持ってくることが可能

stock = soup.find("a", text="삼성전자")
print(stock)