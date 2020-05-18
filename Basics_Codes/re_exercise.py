import re
data = open('Actual data.txt')
sum = 0
for line in data:
    temp = re.findall('[0-9]+',line)
    if len(temp) == 0: continue
    for i in temp:
        sum += int(i)
print(sum)
