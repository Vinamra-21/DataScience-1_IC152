class IC152():                              #defining class
    def __init__(self,name,roll_no,marks):
        self.name=name                      #name
        self.roll_no=roll_no                #roll no
        self.marks=marks                    #marks
    
    def result(self):                       #result function
        if float(self.marks) >=33: 
            return 'pass'
        else:
            return 'fail'

    def input_check():  
        checkr=[]           #splitting roll no
        for i in roll_in:
            checkr+=i
        if len(checkr)==6:                             #roll_no should be of 6 letters
            if checkr[0:3]==['B','2','3']:             #check format of roll no
                for i in range(3,6):
                    if checkr[i] in '1234567890':      #check last three digits of roll no
                        pass 
                    else:
                        print('Invalid Input')
                        exit()
                for i in marks_in:    #check if entered marks are in correct range
                    if i in '+.1234567890':
                        if float(marks_in) < 101 or float(marks_in) >=1: 
                            return True
                        else:
                            print('Invalid Input')
                            exit()
                    else:
                        print('Invalid Input')
                        exit()
                else:
                    print('Invalid Input')
                    exit()
            else:
                print('Invalid Input')
                exit()
        else:
            print('Invalid Input')
            exit()

    

name_in=input('Name of Student:')
roll_in=input('Roll_no of student:')
marks_in=input('marks of student:')


if IC152.input_check()==True:                      #check condition
    student1=IC152(name_in,roll_in,marks_in)       #object
    print(student1.result())                       #print result
    
    