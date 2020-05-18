base=int(input("Enter the number:"))
power=int(input("Enter the power:"))
def powerexp(base,power):
    if(power==1):
        return(base)
    else:
        return(base*powerexp(base,(power-1)))
print("The value is",powerexp(base,power))
