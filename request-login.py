import requests

url = "https://logins.daum.net/accounts/srp.do?slevel=1&rid=2fd29c0d-e41c-4fc3-89f7-d4c25509d554&srplm1=2bd347362e1dc7c2628e91fe8a9d66703d73004033c961928f087299ae0e641b"
data = {
    "url" : "https://www.daum.net",
    "slevel" : "1",
    "luid" : "62a08d70-90b4-4388-a26d-24fc4b60cb29:1527531631613:Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F66.0.3359.181+Safari%2F537.36:121.161.229.68:toploginform",
    "id" : "id",
    "pw" : "heesun23"
}
session = requests.session()
response = session.post(url, data = data)
response.raise_for_status()

print(response.text)


# session.post(url)
# session.put(url)
# session.delete(url)



# https://logins.daum.net/accounts/srp.do?slevel=1&rid=2fd29c0d-e41c-4fc3-89f7-d4c25509d554&srplm1=2bd347362e1dc7c2628e91fe8a9d66703d73004033c961928f087299ae0e641b
# Request Method: POST




# url: https://www.daum.net
# slevel: 1
# luid: 62a08d70-90b4-4388-a26d-24fc4b60cb29:1527531631613:Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F66.0.3359.181+Safari%2F537.36:121.161.229.68:toploginform
# id: ssunder22
# pw: