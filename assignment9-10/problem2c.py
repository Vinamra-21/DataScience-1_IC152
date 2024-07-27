class queue():
    def __init__(self):          #class queue
        self.queue_list=[]       #attribute list
        self.elements=None       #attribute element
    
    def push(self, add_in):   #push function
        self.queue_list=self.queue_list+[add_in]

    def pop(self , pull_out):  #pop function
        if int(len(self.queue_list))==0:
            print('No elements to pop in the stack')
            exit()
        elif pull_out!=self.queue_list[0]:
            print(f'Queue folows LIFO. First element is not {pull_out}')
            exit()
        else:
            self.queue_list=self.queue_list[1:]
            self.elements=pull_out
            print(f'Popped element is:{self.elements}')

    def peek(self):      #peek function
        n=int(len(self.queue_list))
        if n==0:
            print('Queue is empty')
            exit()
        else:
            self.elements=self.queue_list[0]
            print(f'First element is:{self.elements}')    


    
queue1=queue()
queue1.push(1)
queue1.push(2)
queue1.push('abc')
queue1.pop(1)
queue1.peek()