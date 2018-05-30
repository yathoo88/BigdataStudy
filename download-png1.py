import urllib.request
import urllib.parse

api = "https://search.naver.com/search.naver"
values = {
    "where" : "nexearch",
    "sm" : "top_hty",
    "fbm" : "1",
    "ie" : "utf8",
    "query" : "초콜릿"

}

params = urllib.parse.urlencode(values)

url = api +  "?" + params
print("url = ", url)

data = urllib.request.urlopen(url).read()
# print(data)
text = data.decode("utf-8")
print(text)



# https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%B4%88%EC%BD%9C%EB%A6%BF