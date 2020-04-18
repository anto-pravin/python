from urllib.request import urlopen
import json

url = 'http://py4e-data.dr-chuck.net/comments_407715.json'
st = urlopen(url).read()
js = json.loads(st)
sum = 0
for items in js['comments']:
    sum += items['count']
print(sum)