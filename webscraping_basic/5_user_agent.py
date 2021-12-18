import requests
url = "https://sunchichi0229.github.io/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
with open("sunchichiblog.html", "w", encoding="utl8") as f:
    f.write(res.text)