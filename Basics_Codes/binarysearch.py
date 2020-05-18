def Binarysearch(L,n,l,h,key):
    mid=(l+h)//2
    if(L[mid]==key):
        return ("The element is found at index",mid)
    elif(L[mid]>key):
        h=mid-1
        return(Binarysearch(L,n,l,h,key))
    elif(key>L[mid]):
        l=mid+1
        return(Binarysearch(L,n,l,h,key))
    else:
        return(-1)
n=int(input("Enter the number of elements:"))
L=[]
for i in range(n):
    a=int(input("Enter the elements:"))
    L.append(a)
l=0
h=n-1
key=int(input("The element to be searched:"))
val=(Binarysearch(L,n,l,h,key))
if(val==-1):
    print("not found")
else:
    print("element found at index",val)
