def mergesort(L):
    if(len(L)<=1):
        return(L)
    else:
        mid=n//2
        left=mergesort(L[:mid])
        right=mergesort(L[mid:])
        return merge(left,right)
def merge(left,right):
    result=[]
    i=j=0
    while(i<len(left))and(j<len(right):
        if(left[i]<=right[j]):
            result.append(Left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i]
    result+=right[j]
n=int(input(""))
L=[int(input(""))for i in range(n)]
mergesort(L)
print(L)
