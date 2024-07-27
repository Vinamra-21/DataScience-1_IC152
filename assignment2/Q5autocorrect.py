import os
with open(os.path.expanduser('~') + '/Desktop/B23302_assignment2/inputWithErrors.txt') as f:lines= [line.rstrip() for line in f]

print(lines)

newlineFinal=[]
for line in lines:
    newlineFinal.append(line.capitalize().replace(' ,',',').replace('(',' (').replace(' )',')').replace('windows','Windows').replace('python','Python').replace('macintosh','Macintosh').replace('google','Google').replace('linux','Linux').replace('c++','C++').replace('java','Java'))
# The above code capitalizes every item of the list 'lines' ,corrects the position of paranthesis, extra space, and capitalizes some of the words.

newlineFinal[0]=newlineFinal[0].title()
newlineFinal[3]=newlineFinal[3].replace('though','Though')
newlineFinal[5]=newlineFinal[5].replace('c','C').replace('C','c',2)
newlineFinal[7]=newlineFinal[7].replace('you','You',1)
newlineFinal[8]=newlineFinal[8].replace('you','You')
#The above code also corrects some of the errors which could'nt be done inside the for loop. 

fOutput = open(os.path.expanduser('~') + '/Desktop/B23302_assignment2/outputClean.txt', 'w')

fOutput.write("\n".join(newlineFinal)  )
fOutput.close()    

