def swap(L,i,j):
    temp=L[i]
    L[i]=L[j]
    L[j]=temp
n=int(input("Enter the number of elements:"))
L=[int(input("Enter the element:")) for i in range(n)]
for i in range(n):
    least=L[i]
    for j in range(i+1,n):
        if(L[j]<least):
            least=L[j]
        j=L.index(least)
        swap(L,i,j)
print(L)
