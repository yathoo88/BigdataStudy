import urllib.request
from bs4 import BeautifulSoup

url = "http://info.finance.naver.com/marketindex/"
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, 'html.parser')
#soup.select_one()
results = soup.select("a.head.usd > div.head_info > span.value")

for result in results :
    print(result.string);