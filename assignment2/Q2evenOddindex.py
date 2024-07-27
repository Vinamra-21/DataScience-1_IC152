#Extracting Even and Odd index characteres of a string.
string='Hello World'

evenPosStr=string[0:len(string)+1:2] #takes even place characters
oddPosStr=string[1:len(string)+1:2]  #takes odd place characters

print(evenPosStr+oddPosStr)
