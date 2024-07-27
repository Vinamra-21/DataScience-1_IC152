#q3 part a
#Is leap year
def IsleapYear():
    b=int(input('q3 part -a input (year):'))
    if (b%4==0 and b%100!=0) or (b%400==0):
        print(b,'Is a leap year.')
    else:
        print(b,'Is not a leap year.')
    
IsleapYear()
    

#q3 part b
#Type of triangle
def TriangleType():
    a=int(input('q4 part b input (integer):'))
    b=int(input('q4 part b input (integer):'))
    c=int(input('q4 part b input (integer):'))
    if (a==b==c):
        print('Triangle is Equilateral')
    elif (a==b and b!=c and a!=c)or(b==c and a!=c and b!=a)or(a==b and a!=c and b!=c):
        print('Triangle is Isoceles')
    else:
        print('Triangle is Scalar')
    
TriangleType()





   