import requests

res = requests.get("https://www.google.com/")

# res = requests.get("https://www.naver.com/")
res.raise_for_status()

# print("응답코드 :", res.status_code)

# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     print("에러코드", res.status_code)

print(len(res.text))

print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
