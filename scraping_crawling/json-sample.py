import urllib.request as request
import json

json_str = request.urlopen("https://api.github.com/repositories").read().decode('utf-8')

output = json.loads(json_str)


for item in output :
    print(item["name"])
