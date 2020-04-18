n=int(input("Enter the number:"))
L=[]
while(n>0):
    digit=n%10
    L.append(digit)
    n=n//10
K=L[:]
K.reverse()
if(L==K):
    print("palindrome")
else:
    print("Not a palindrome")
