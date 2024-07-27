user_input=input('Enter a string:')
x=int(len(user_input))

if(len(user_input)%2==0):
    firstPartOfStr=user_input[0:int(x/2)]
    secondPartOfStr=user_input[int(x/2):]
else:
    firstPartOfStr=user_input[0:int((x+1)/2)]
    secondPartOfStr=user_input[int(((x+1)/2)+1):]
#The if statement determines if the word entered has even or odd characters.
#Then executes respective instruction given as mentioned in the quesetion.

revSecondPartOfStr=secondPartOfStr[::-1]
#[::-1]:-Reverses the string.
print(firstPartOfStr+revSecondPartOfStr)
