#q2 part a 
#positive input printer
a=input('q2 part a- input (string):')
digits='0123456789'
firstIter=True
for char in a:
    if (char in digits) :
        pass
    elif (char in '+') and (firstIter):
        pass
    else:
        exit()
    firstIter=False
print(a)

           
#q2 part 
#positive(1)   negative(-1)    zero(0)
a=int(input('q2 part b- input (integer):'))
if a>0:
    print(1)
elif a==0:
    print(0)
else:
    print(-1)


#q2 part c
#alpha digit or both
a=input('q2 part c- input (string):')
if a.isdigit()==True:
       print('The string consists of only digits')
elif a.isalpha()==True:
    print('The string consists of only alphabets')
elif a.isalnum()==True:
    print('The string consists of alphabets and digits both')
else:
    print('The string neither consists of alphabets nor digits')


#q2 part d
#number of days in month
a=input('q2 part d- input (month):')
b=int(input('q2 part d- input (year):'))
if (b%4==0 and b%100!=0) or (b%400==0):
    if (a=='January'|'March'|'May'|'July'|'August'|'October'|'December'):
        print(31)
    elif(a=='February'):
        print(29)
    else:
        print(30)
else:
    if (a=='January'|'March'|'May'|'July'|'August'|'October'|'December'):
        print(31)
    elif(a=='February'):
        print(28)
    else:
        print(30)
        

#q2 part e
#maximum of three numbers
a=input('q2 part e- input (integer):')
b=input('q2 part e- input (integer):')
c=input('q2 part e- input (integer):')
print('Max=',max(a,b,c))



        
