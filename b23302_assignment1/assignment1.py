
#1a
print(2|3)
print(bin(2))
print(bin(3))
print(bin(2|3))

#1b
x=int(input('Enter a number:'))
o=1
if(x&o==1):
  print('number is odd,1')
else:
    print('number is even,0')

#1c
print(24>>1)
print(bin(24))
print(bin(12))

#2a
print(27/8)

#2b
print(27//8)

#2c
print(27>>3)
# as 27 in binary is 0b11011 and 8 means 2^3 so ans is 3 bin 0b11
#2d
print(2**10)
print(2**20)
print(1<<10)
print(2<<10)

#2e
num=('enter a binary containing only 1')
print(2**len(num)-1)

#3a
print(-5,7)

#3b
import math
for i in range(1,10):
   for j in range(1,16):
    if (math.pow(i,3)+math.pow(j,3))==1729:
      print(i,j)

#4a
print(50-3*10 , (50-3)*10)

#4b
import math
print(math.log(4096,2))

#4c
import math
def sqroot(a,b,c):
  x1=(-b+math.sqrt((b**2)-(4*a*c)))/(2*a)
  x2=(-b-math.sqrt((b**2)-(4*a*c)))/(2*a)
  print(x2,x1)

#5a
x=-14.125
bin=1100000000101100010000000000000000000000000000000000
'''first 1 is binary for - sign
   then let it be 8 X 1.765625
   implies s=1 , e=1026 , f=.765625
   then refer assignment'''
 
#5b
# binary to decimal
#(-)8 X(1+2^-1+2^-2+2^-6)
#=-14.125
