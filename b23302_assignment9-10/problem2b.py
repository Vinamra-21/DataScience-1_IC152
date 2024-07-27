class stack():                #class stack
    def __init__(self):
        self.stack_list=[]    #attribute list
        self.elements=None    #attribute elements
      
    def push(self, add_in):   #push function
        self.stack_list=self.stack_list+[add_in]

    def pop(self , pull_out):  #pop function
        n=int(len(self.stack_list))
        if n==0:
            print('No elements to pop in the stack')
            exit()
        elif pull_out!=self.stack_list[-1]:
            print(f'Stack folows LIFO. First element is not {pull_out}')
            exit()
        else:
            self.stack_list=self.stack_list[0:(n-1)]
            self.elements=pull_out
            print(f'Popped element is:{self.elements}')

    def peek(self):      #peek function
        n=int(len(self.stack_list))
        if n==0:
            print('stack is empty')
            exit()
        else:
            self.elements=self.stack_list[-1]
            print(f'Topmost element is:{self.elements}')
    
    
stack1=stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push('abc')
stack1.pop('abc')
stack1.peek()


   

 