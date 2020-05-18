def linear(L,key):
    for i in L:
        if(i==key):
            return(1)
n=int(input("Enter the number of elememt:"))
L=[int(input("Enter the element:"))for i in range(n)]
key=int(input("Enter the element to bee searched:"))
if(linear(L,key)==1):
    print("Element found")
else:
    print("element not found")
