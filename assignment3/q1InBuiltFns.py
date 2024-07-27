#q1 part a

#difference between outputs of round() and format()
print(round(23.5312,3))
print(format(23.5312,'.3f'))
#the  round() function rounds the float to the nearest integer
#and format() function just removes the number or add zero at end to get the desired length of decimal

import math

#rounds the float values to nearest integer on right side of number line.
print(math.ceil(3.14))
print(math.ceil(3.5))
print(math.ceil(3.9))

#rounds the float values to nearest integer on left side of number line.
print(math.floor(3.14))
print(math.floor(3.5))
print(math.floor(3.9))

#rounds the float values to nearest integer.
print(round(3.14))
print(round(3.5))
print(round(3.9))
print(round(3.145,2))
print(round(3.155,2))
print(round(3.95,1))
print(round(3.91,1))

#rounds the float values to nearest integer and [type()=int] indicates that round() has converted float to integer.
print(type(round(3.14)))
print(type(round(3.5)))
print(type(round(3.9)))

#format() is used to make a number of the desired decimal length without rounding.
print(format(3.143,'.2f'))
print(format(3.5,'.2f'))
print(format(3.9,'.3f'))

#format() is used to make a number of the desired decimal length without rounding and float gets converted to string after this operation.
print(type(format(3.14)))
print(type(format(3.5)))
print(type(format(3.9)))

#q1 part b
# Use following string methods on different characters and numbers
str1=''
str2='23'
str3='qq1b'
a=str1.isalpha()
b=str1.isspace()
c=str1.isnumeric()
d=str1.isalnum()
e=str2.isalpha()
f=str2.isspace()
g=str2.isnumeric()
h=str2.isalnum()
i=str3.isalpha()
j=str3.isspace()
k=str3.isnumeric()
l=str3.isalnum()
finalList=[a,b,c,d,e,f,g,h,i,j,k,l]
print(finalList)

