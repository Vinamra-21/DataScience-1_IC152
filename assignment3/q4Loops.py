#q4 part a 
#string reversing without using [::-1]
a = input("q4 part a input (string):")
reversed_string =""
for n in range(0,len(a)):
      reversed_string += a[len(a)-n-1]
print(reversed_string)


#q4 part b
#sum of odd and even integers
b = int(input("q4 part b input (integer):"))
oddSum = 0
evenSum = 0 
for a in range(0,b,2):
    evenSum += a
for b in range(1,b,2):
     oddSum += b

print(evenSum , oddSum)


#q4 part c
#Factorial of N
N = int(input("q4 part c input (integer):"))
N_Factorial = 1
i = 1
if N > 1:
    while i<=N:
        N_Factorial *= i
        i += 1
else :
    N_Factorial = 1
print(N_Factorial)

        



     

