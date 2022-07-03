import requests

res = requests.get("https://www.naver.com/")
print("응답코드 :", res.status_code)

if res.status_code == requests.codes.ok:
    print("정상입니다")
else:
    