n=int(input("Enter the number:"))
a=b=n
count=0
sum=0
while(n>0):
    dig=n%10
    count+=1
    n=n//10
while(a>0):
    digit=a%10
    sum+=(digit**count)
    a=a//10
if(b==sum):
    print("Armstrong number")
else:
    print("Not an armstrong")
