#Problem_3-part_a

def prefRevCapStr(user_string, i, n):
    if i == n:
        return user_string[n-i].upper() + " -> " + user_string
        #when the whole string is reversed then we add arrow and string.
    else:
        return user_string[n-i].upper() + prefRevCapStr(user_string, i+1,n)
        #capitalizes all the characters of the string and concactenates from the back. 


user_string=input('Enter a string:')
print(prefRevCapStr(user_string, 0, len(user_string)-1))
##EXAMPLE##
user_string='Holi-to-come'
print(prefRevCapStr(user_string, 0, len(user_string)-1))

######################################################################################################################################

#Problem_3-part_b
def scatSubStr(w,s):
    if w == '':
        return 'yes'
    else:
        if(w[0] in s):
            return scatSubStr(w[1:],s[s.find(w[0]):])
            #basically slices the string according to the letters similar in both w and s till all the letters in w are done.
        else:
            return 'false'


w=input('Enter a string(w):')
s=input('Enter a string(s):')
print(scatSubStr(w,s))
##EXAMPLE##
w = 'abb'
s = 'cadbebb'
print(scatSubStr(w,s))


