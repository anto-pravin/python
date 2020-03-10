def reverse(string, result): # The function will return the reverse String
    if not string:
        return result
    else:
        LastCharacter = string[-1]
        return reverse( string[:-1], result + LastCharacter )
string = input() # Enter the String input
result = ''
print(reverse(string, result))
