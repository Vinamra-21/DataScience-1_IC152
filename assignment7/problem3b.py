#importing required modules
import numpy as np
import matplotlib.pyplot as plt

# loop for all plots
for i in (5,50): 
  sample_space=[]
  for j in range(50000):
    yList=[]
    for k in range(i+1):
      outcome=np.random.randint(0,4)
      yList.append(outcome)
    sample_space.append(sum(yList)/5)

  #plotting graph and defining characteristics of graph
  plt.hist(sample_space,bins=80)
  plt.grid(True)
  plt.xlabel('sample means (observed values)')
  plt.ylabel('frequency')
  plt.title(f'problem3b_{i}_50000')
  plt.savefig(f'problem3b_{i}_50000.png')
  plt.clf()
     
