import requests

from bs4 import BeautifulSoup

url = "https://www.kccwf.or.kr/home/comm/comm0001m01/mainPage.html"
res - requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

print(suop.a.attrs)
