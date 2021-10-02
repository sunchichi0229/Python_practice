import requests
from bs4 import BeautifulSoup

#種目コードリスト
codes = [
    '9434.T',
    '7974.T',
    '7203.T'
]

for code in codes:
    url = f"https://finance.yahoo.co.jp/quote/{code}"

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select_one("._3rXWJKZF").text
    price = price.replace(',', '')
    print(price)