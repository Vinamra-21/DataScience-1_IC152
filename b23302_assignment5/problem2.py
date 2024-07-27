#Probem_2-part_a

#recurssion function for f(n)
def f(n):
    if n<2:
        return 1
    else:
        return 1.65*f(n-1)
    
#taking input,calling the function and printing output
n=int(input('Enter an integer:'))
print(f'f({n})=',f(n))

#recurssion function for g(n)
def g(n):
    if n<2:
        return 1
    else:
        return g(n-1)+g(n-2)
    
#taking input,calling the function and printing output
n=int(input('Enter an integer:'))
print(f'g({n})=',g(n))

#recurssion function for h(n)
def h(n):
    if n<2:
        return 2
    else:
        return 2*h(n-2)
    
#taking input,calling the function and printing output
n=int(input('Enter an integer:'))
print(f'h({n})=',h(n))

#recurssion function for k(n)
def k(n):
    if n<3:
        return 3
    else:
        return k(n-1)+k(n-3)
    
#taking input,calling the function and printing output
n=int(input('Enter an integer:'))
print(f'k({n})=',k(n))

#######################################################################################################################

#Problem_2-pat_b

#importing required modules
import numpy as np
import matplotlib.pyplot as plt

#making subplots defination, defining number of rows and columns
fig,axes=plt.subplots(figsize=(10,10),nrows=2,ncols=2)

#main title
fig.suptitle('Problem_1-Part_b')

#array of values for x-axis
xValues=[np.arange(0,10)]

#y-axis values for first subplot
yValues1=[]
for i in range(0,10):
    yValues1.append(f(i))


#plot scatter graph
axes[0][0].scatter(xValues,yValues1)

#set labels for x and y axis
axes[0][0].set_xlabel('Values',fontsize=12)
axes[0][0].set_ylabel('f(n)',fontsize=12)

#display grid
axes[0][0].grid(True)


#y-axis values for second subplot
yValues2=[]
for i in range(0,10):
    yValues2.append(g(i))

#plot scatter graph
axes[0][1].scatter(xValues,yValues2)

#set labels for x and y axis
axes[0][1].set_xlabel('Values',fontsize=12)
axes[0][1].set_ylabel('g(n)',fontsize=12)

#display grid
axes[0][1].grid(True)

#y-axis values for third subplot
yValues3=[]
for i in range(0,10):
    yValues3.append(h(i))

#plot scatter graph
axes[1][0].scatter(xValues,yValues3)

#set labels for x and y axis
axes[1][0].set_xlabel('Values',fontsize=12)
axes[1][0].set_ylabel('h(n)',fontsize=12)

#display grid
axes[1][0].grid(True)

#y-axis values for fourth subplot
yValues4=[]
for i in range(0,10):
    yValues4.append(k(i))

#plot scatter graph
axes[1][1].scatter(xValues,yValues4)

#set labels for x and y axis
axes[1][1].set_xlabel('Values',fontsize=12)
axes[1][1].set_ylabel('k(n)',fontsize=12)

#display grid
axes[1][1].grid(True)

plt.tight_layout()
plt.subplots_adjust(hspace=.25,bottom=.09)
#save the graph
plt.savefig('fig-2(b).jpeg')
#show the plot
plt.show()

################################################################################################################################
#Problem_2-part_c

#Values for x-axis
xValues=[]
for i in range(0,10):
    xValues.append(i)

#Values for y-axis(plot curve 1)
yValues1=[]
for i in range(0,10):
    yValues1.append(f(i))

#Values for y-axis(plot curve 2)
yValues2=[]
for i in range(0,10):
    yValues2.append(g(i))

#Values for y-axis(plot curve 3)
yValues3=[]
for i in range(0,10):
    yValues3.append(h(i))

#Values for y-axis(plot curve 4)
yValues4=[]
for i in range(0,10):
    yValues4.append(k(i))

#plotting all the curves on single graph
plt.plot(xValues,yValues1,label='f(n)')
plt.plot(xValues,yValues2,label='g(n)')
plt.plot(xValues,yValues3,label='h(n)')
plt.plot(xValues,yValues4,label='k(n)')

#define x-axis range
plt.xlim(0,10)

#define y-axis range
plt.ylim(0,80)

#defining x and y labels
plt.xlabel('inputs')
plt.ylabel('outputs')

#show grid
plt.grid(True)

#show legend
plt.legend()

plt.tight_layout()
#save the graph
plt.savefig('fig-2(c1).jpeg')
#show the plot
plt.show()

#####FOR LARGER RANGES#####

#Values for x-axis
xValues=[]
for i in range(0,20):
    xValues.append(i)

#Values for y-axis(plot curve 1)
yValues1=[]
for i in range(0,20):
    yValues1.append(f(i))

#Values for y-axis(plot curve 2)
yValues2=[]
for i in range(0,20):
    yValues2.append(g(i))

#Values for y-axis(plot curve 3)
yValues3=[]
for i in range(0,20):
    yValues3.append(h(i))

#Values for y-axis(plot curve 4)
yValues4=[]
for i in range(0,20):
    yValues4.append(k(i))

#plotting all the curves on single graph
plt.plot(xValues,yValues1,label='f(n)')
plt.plot(xValues,yValues2,label='g(n)')
plt.plot(xValues,yValues3,label='h(n)')
plt.plot(xValues,yValues4,label='k(n)')

#defining x and y labels
plt.xlabel('inputs')
plt.ylabel('outputs')

#show grid
plt.grid(True)

#show legend
plt.legend()

plt.tight_layout()
#save the graph
plt.savefig('fig-2(c2).jpeg')
#show the plot
plt.show()


###OBSERVATIONS ON LARGER RANGES###
print('---Observations on larger ranges---')
print('graph of f(n) and g(n) goes on increasing and approaces to a very large value')
print('slope of h(n) is less steep')
print('value of k(n) increases slowly in steps')