import requests
res = requests.get("http://google.com")
res.raise_for_status()

print("応答コード :", res.status_code) #200なら正常

# if res.status_code == requests.codes.ok:
#     print("正常です")
# else:
#     print("問題が置きました。[Error Code ", res.status_code, "]")

print(len(res.text))

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)