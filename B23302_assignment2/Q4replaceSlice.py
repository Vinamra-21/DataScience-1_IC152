string='Anyone can learn python , python is so easy. The best way to learn python is using it for different tasks.'
#1

nString=string.replace('python','coding')
print(nString)
nnString=nString.replace('coding','python',2)
print(nnString)
nnnString=nnString.replace('python','coding',1)
print(nnnString)

#First We replace all the words(python) to coding.
#Second We replace first 2 words(coding) with python. 
#Third We replace only the first word(python) to coding.

#2

print(string[:int(string.find('python')-1)],'coding ,'+string[int(string.find('python')+8):int(string.rfind('python')-1)]+' coding '+string[int(string.rfind('python')+7):])
#In this method we slice up the given string except the words which we want to replace.

#3

print(string[:string.find('python')+len('python')].replace('python','coding') + string[string.find('python')+len('python'):string.rfind('python')] + string[string.rfind('python'):].replace('python','coding'))
#This method is a hybrid of 1st and 2nd methods.Its logic is easy to come up with.

#method one is easy but lengthy to type but method 2,3 are short and tidious to think.
#First method there are less chances to making a mistake as we have to use less syntax.
#2nd and 3rd methods have a high change of getting a syntax error as we have to use string methods,paranthesis,etc.