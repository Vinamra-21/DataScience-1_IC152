#problem_1 part_a

import problem0 as pb

#Highest = the state with the highest value
def highestP1(n):

    a=0
    b=0
    c=0
    #if any b is larger than a then it replaces a otherwise loop goes onto next b 
    for i in range(0,len(pb.data)):
        b=pb.data[i][n]
        if b>a:
            a=b
            c=pb.data[i][0]
    #printing the corresponding state
    print('highest value is of state-',c)

#Lowest = the state with the lowest value
def lowestP1(n):
    #making dictionary,sorting it wrt values and taking the first key as answer
    dict1={}
    for i in range(0,len(pb.data)):
       dict1[pb.data[i][0]]=pb.data[i][n]
    sorted_dict = dict(sorted(dict1.items(), key=lambda item: item[1]))
    ans=list(sorted_dict.keys())[0]
    print('lowest value is of state-',ans)

#Median = the median
def medianP1(n):
    #defining list of the required elements
    lst1=[]
    for i in range(0,len(pb.data)):
        lst1.append(pb.data[i][n])
    lst1.sort()
    #check for even or odd number of elements
    if len(lst1)%2==0:
        median=[lst1[int(len(lst1)/2)],lst1[int(len(lst1)/2+1)]]
    else:
        median=lst1[len(lst1)+1/2]
    #printing median
    print('median is',median)

#Average = the average value
def averageP1(n):
    #adding all the required elements and then dividing by the  number of elements
    sum=0
    for i in range(0,len(pb.data)):
        b=pb.data[i][n]
        sum+=b
    sum=sum/12
    #printing average
    print('average is',sum)

#Mode = the value with highest frequency
def modeP1(n):
    lst3=[]
    #defining list of the required elements
    for i in range(0,len(pb.data)):
        lst3.append(pb.data[i][n])
    #counting the number of elements
    for i in lst3:
        a=0
        b=lst3.count(i)
        #assigning a variable 'mode' to the value having highest frequency
        if b>a:
            mode=i
        else:
            pass
    #printing mode
    print('mode is',mode,'\n')
        

#i)population density

#Highest = the state with the highest value
highestP1(6)

#Lowest = the state with the lowest value
lowestP1(6)

#Median = the median
medianP1(6)

#Average = the average value
averageP1(6)

#Mode = the value with highest frequency
modeP1(6)


#ii) percentage of marginal farmers

#Highest = the state with the highest value
highestP1(7)

#Lowest = the state with the lowest value
lowestP1(7)

#Median = the median
medianP1(7)

#Average = the average value
averageP1(7)

#Mode = the value with highest frequency
modeP1(7)


#iii)percentage of women in the overall workforce

#Highest = the state with the highest value
highestP1(11)

#Lowest = the state with the lowest value
lowestP1(11)

#Median = the median
medianP1(11)

#Average = the average value
averageP1(11)

#Mode = the value with highest frequency
modeP1(11)

#####################################################################################################################################

#problem_1 part_b

#importing required modules
import numpy as np
import matplotlib.pyplot as plt

w=0.4

#defining value for first part of the multiple bar graph
yList1=[]
for i in range(0,len(pb.data)):
    yList1.append(pb.data[i][4])
sum1=sum(yList1)
#expressing in percentage to make it readable
ynew_list1=[]
for i in range(0,len(yList1)):
    ynew_list1.append((yList1[i]/sum1)*100)

#defining value for second part of the multiple bar graph
yList2=[]
for i in range(0,len(pb.data)):
    yList2.append(pb.data[i][5])
sum2=sum(yList2)
#expressing in percentage to make it readable
ynew_list2=[]
for i in range(0,len(yList2)):
    ynew_list2.append((yList2[i]/sum2)*100)

#defining value for x-axis
xList=[]
for i in range(0,len(pb.data)):
    xList.append(pb.data[i][0])

#defining initial x-axis marks and placement of bars
bar1=np.arange(len(xList))
bar2=[i+w for i in bar1]

#display grid
plt.grid(True)

#plotting the graph using the values defined above
plt.bar(bar1, ynew_list1, width=w, label='the percentage area with slope > 30%(%)')
plt.bar(bar2, ynew_list2, width=w, label='the road density(%)')

#display legend
plt.legend()

#Title for graph
plt.title('the percentage area with slope > 30%(%)|the road density(%) vs states')

#spacing marks on x-axis
plt.xticks(bar1+w/2,xList,rotation=45)

#range of y-axis
plt.ylim(0,30)

plt.tight_layout()
#save the graph
plt.savefig('fig-1(b).jpeg')
#show the plot
plt.show()

#############################################################################################################################

#problem_1 part_c

#importing required modules
import numpy as np
import matplotlib.pyplot as plt

w=0.4

#making new dictionary to collect the data
new_dict={}
for i in range(0,len(pb.data)):
    new_dict[pb.data[i][0]]=pb.data[i][4]

#sorting the data according to the values
sorted_dict = dict(sorted(new_dict.items(), key=lambda item: item[1]))

#values for x-axis
xList=sorted_dict.keys()

#defining list for y-axis elements
yList=[]
for i in range(0,len(pb.data)):
    yList.append(pb.data[i][5])

#initial x-axis marks
bar1=np.arange(len(xList))

#display grid(only horizontal)
plt.grid(axis='y')

#plotting bar graph
plt.bar(bar1, yList, width=w, label='the road density')

#display legend
plt.legend()

#display title
plt.title('Problem_1-part_c')

#marks on x-axis
plt.xticks(bar1,xList,rotation=45)

plt.tight_layout()
#save the graph
plt.savefig('fig-1(c).jpeg')
#show the plot
plt.show()