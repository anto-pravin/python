import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


url = 'http://py4e-data.dr-chuck.net/known_by_Kirsteen.html'
number = int(input())
times = int(input())

# Retrieve all of the anchor tags
for i in range(times):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    k = 0
    for tag in tags:
        if k == number-1:
            url = tag.get('href',None)
            break
        k+=1
print(url)

        