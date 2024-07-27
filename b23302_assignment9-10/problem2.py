class stack():                #class stack
    def __init__(self):
        self.stack_list=[]    #attribute list
      
    def push(self, add_in):   #push function
        self.stack_list=self.stack_list+[add_in]

    def pop(self , pull_out):  #pop function
        n=int(len(self.stack_list))
        if n==0:
            print('0')
            exit()
        elif pull_out!=self.stack_list[-1]:
            print('0')
            exit()
        else:
            self.stack_list=self.stack_list[0:(n-1)]
    def CountStack(self):  #to check length of stack
        if int(len(self.stack_list))==0:
            print('1')
        else:
            print('0')

string1=input('Please enter a string(string of single-digit integers, binary operands and brackets/parentheses):') #input string
lst=[]  #each element of the string
for i in string1.split():
    for j in i:
      lst.append(j)
stack1=stack() #object
#main program to check find out if the brackets/parentheses are balanced.
for i in lst: 
    if i in '([{':
        stack1.push(i)
    elif i in ')]}':
        if i==')':
            stack1.pop('(')
        elif i==']':
            stack1.pop('[')
        else:
            stack1.pop('{')
    else:
        pass
stack1.CountStack()



   

 