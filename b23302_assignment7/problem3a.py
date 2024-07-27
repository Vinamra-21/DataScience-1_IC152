#importing required modules
import numpy as np
import matplotlib.pyplot as plt

#loop for all plots
for i in (50,500,5000,50000):
    xList=[] 
    rel_freq_lst0=[]
    rel_freq_lst1=[]
    rel_freq_lst2=[]
    rel_freq_lst3=[]
    yList=[]
    for j in range(i):
        xList.append((j+1))
        outcome=np.random.randint(0,4)
        yList.append(outcome)
        freq0=yList.count(0)
        freq1=yList.count(1)
        freq2=yList.count(2)  
        freq3=yList.count(3)
        rel_freq_lst0.append(freq0/(j+1)) #relative frequency of 0
        rel_freq_lst1.append(freq1/(j+1)) #relative frequency of 1
        rel_freq_lst2.append(freq2/(j+1)) #relative frequency of 2
        rel_freq_lst3.append(freq3/(j+1)) #relative frequency of 3
        
    #plotting graph and defining characteristics of graph
    plt.plot(xList,rel_freq_lst0 , label='relative frequency of 0')
    plt.plot(xList,rel_freq_lst1 , label='relative frequency of 1')
    plt.plot(xList,rel_freq_lst2 , label='relative frequency of 2')
    plt.plot(xList,rel_freq_lst3 , label='relative frequency of 3')
    plt.legend()
    plt.grid(True)
    plt.xlabel('number of trials')
    plt.ylabel('relative frequency')
    plt.title(f'problem3a_{i}')
    plt.savefig(f'problem3a_{i}.png')
    plt.clf()
     

    
        

