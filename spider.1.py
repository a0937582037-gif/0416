import requests
from bs4 import BeautifulSoup

url = "https://20260416-xi.vercel.app/about"
Data = requests.get(url)
Data.encoding = "utf-8"
#print(Data.text)
sp = BeautifulSoup(Data.text, "html.parser")
result=sp.select("td iframe")
for item in result:
	print(item.get("src"))
