def GCD(x,y):
    rem=x%y
    if(rem==0):
        return(y)
    else:
        return GCD(y,rem)
x=int(input("Enter a number:"))
y=int(input("Enter another number:"))
print("the greatest common divisor is",GCD(x,y))
