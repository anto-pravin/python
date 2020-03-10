Number = int(input())
ReversedNumber = 0
while Number != 0:
    LastDigit = Number % 10
    ReversedNumber = ( ReversedNumber * 10 ) + LastDigit
    Number //= 10
print(ReversedNumber)