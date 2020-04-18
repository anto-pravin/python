a=input("enter file name")
f1=open(a,"w")
n=int(input("size of input"))
for i in range(n):
    f1.write(input("input"))
    f1.write(("\n")*2)
f1.close()
count1=0
count2=0
with(open(a,"r")) as f:
    for line in f:
        count1+=1
        word=line.split()
        for i in word:
            count2+=1
print(count1)
print(count2)
