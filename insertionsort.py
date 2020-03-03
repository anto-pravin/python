def insertionsort(L,n):
    for i in range(n):
        value=L[i]
        j=i-1
        while(j>=0)and(L[j]>value):
            L[j+1]=L[j]
            j=j-1
        L[j+1]=value
n=int(input("Enter the number of elements"))
L=[int(input("Enter the elements"))for i in range(n)]
insertionsort(L,n)
print(L)
