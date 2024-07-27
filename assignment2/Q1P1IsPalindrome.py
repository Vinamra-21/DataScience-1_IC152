#Palindrome test
print('Hello,We can check if the entered string is palindrome or not')

user_input = input('Enter a string:')
reverse = user_input[::-1]
#[::-1] :- Reverses the string

if (user_input == reverse):
    print('It is a palindrome')
else:
    print('It is not a palindrome')

#Example:'aba','abcba' are palindromes

