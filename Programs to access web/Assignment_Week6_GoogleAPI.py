import urllib.request, urllib.parse, urllib.error
import json

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

address = input('Enter the location: ')
parameters = dict()
parameters['address'] = address
parameters['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parameters)
    
s = urllib.request.urlopen(url).read().decode()

data = json.loads(s)
js = data['results']
for i in js:
    print(i['place_id'])