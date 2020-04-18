n=int(input("enter the number of elements:"))
L=[]
for i in range(n):
    a=int(input("Enter the element:"))
    L.append(a)
key=int(input("Enter the element to be searched:"))
def Linearsearch(L,n,key):
    for i in range(n):
        if(L[i]==key):
            return(1)
t=Linearsearch(L,n,key)
if (t==1):
    print("The element is present")
else:
    print("Element not found")
