def prime(n):
    for i in range(2,n//2):
        if(n%i==0):
            return(0)
    return(1)
n=int(input("Number"))
p=[]
i=2
while(len(p)<n):
    if(prime(i)==1):
        p.append(i)
    i=i+1
print(p)
