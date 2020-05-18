n=input("Enter the string:")
count=0
for i in n:
    if i in "aeiouAEUOI":
        count+=1
print(count)
