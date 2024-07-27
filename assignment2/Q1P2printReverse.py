#String reversing 
string='This programme will print reversed and original string in the same line.'
print(len(string))

reverse1= string[-1:-len(string)-1:-1]
#[-1:-len(string)-1:-1] :- Here we have subtracted 1 from -len(string) because -len(string) wil slice only upto the 2nd letter of the string. 

reverse2= reverse1[len(string)::-1]
print(reverse1,reverse2)
