from urllib.request import urlopen
import xml.etree.ElementTree as et

url = 'http://py4e-data.dr-chuck.net/comments_407714.xml'
a = urlopen(url).read()

commentinfo = et.fromstring(a)
lst = commentinfo.findall('comments/comment')
sum = 0
for comment in lst:
    sum += int(comment.find('count').text)
print(sum)