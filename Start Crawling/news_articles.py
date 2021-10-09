import requests
from bs4 import BeautifulSoup
import time

response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
articles = soup.select("div.info_group") #newsの記事 div 10個

for article in articles:
    links = article.select("a.info") #リスト
    if len(links) >= 2: #リンクが2個以上であれば
        url = links[1].attrs['href'] #二つ目のリンクのhrefを使用
        response = requests.get(url, headers={'Users-agent':'Mozila/5.0'})
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        content = soup.select_one("#articleBodyContents")
        print(content.text)
        time.sleep(0.3)