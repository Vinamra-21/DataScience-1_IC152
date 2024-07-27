#q5 part a
#prime or not
a = int(input("q5 part a input(natural number):"))
def isprime(n):
    if n <= 1:
        return False
    elif n ==2:
        return True
    elif n % 2 == 0:
        return False
    for i in range (3,n,2):
        if n % i == 0:
            return False
    return True    

if isprime(a):
    print(a, "is a prime number ")
else:
    print(a , 'is not a prime number')
           

#q5 part b
#vowel-dominant or consonant-dominant
b = input("q5 part b input (string):")
vowels = ['a','e','i','o','u']
no_of_vowels = 0
no_of_consonants = 0
for char in b:
    if char  in vowels:
        no_of_vowels += 1
    else :
        no_of_consonants +=1

if no_of_vowels > no_of_consonants:
    print("The word is a vowel dominant word.")
else:
    print("The word is a consonant dominant word.")


#q5 part c
#digit counter
c =input("q5 part c input (string):")
def counting_digits():
    no_of_digits = 0
    for char in c:
        if char.isdigit()==True:
            no_of_digits += 1
        else:
            pass
    print('The given string has' , no_of_digits ,'digits')

counting_digits()


#q5 part d
#letter counter
d = input("q5 part d input (string)")
no_of_letters = 0
for char in d:
    if char.isalpha():
        no_of_letters += 1
    else:
        pass
print('The given string has ', no_of_letters ,'number of letters.')


#q5 part e
#divisors
e = int(input("q5 part e input (integer):"))
list=[]
def divisor():
    for i in range(1,e+1):
     if (e%i==0):
        list.append(i)
    print(list)

divisor()


