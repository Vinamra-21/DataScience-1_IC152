
import matplotlib.pyplot as plt
import numpy as np

xValues, yValues = [], []
scatteredness = 0.2
m = 2
c = 3
for i in range(40):
    for j in range(40-i):
        xValues.append(i + i*np.random.normal(0,scatteredness))
        yValues.append(m*i + i*np.random.normal(0,scatteredness) + c)
xValues.append(100)
yValues.append(10000)

plt.xlabel('Random x values', fontsize = 24)
plt.ylabel('Random y values', fontsize = 24)
plt.title('Increasing gaussian noise added to x and y in y = x',fontsize = 35)
# plt.show()


# once problem is solved, try removing outlier (100,10000) by
# uncommenting (remove ''') following lines:
xValues = xValues[:-1]
yValues = yValues[:-1]

# Estimating m
n = len(xValues)
xValues = np.array(xValues)
#write formulae of numerator and denominator of m below:-
mNum = ((n*np.sum(xValues*yValues))-(np.sum(xValues)*np.sum(yValues)))
mDen = ((n*np.sum(xValues*xValues))-((np.sum(xValues))**2))
mEst = mNum/mDen
print(mEst)


# Estimating c
# write formulae for c below:-
cEst = (1/n)*(sum(yValues) - mEst*sum(xValues))
print(cEst)

# dropping outlier/last element (100,10000) only in the view to zoomin:-
plt.xlim(0,max(xValues[:-1]))
plt.ylim(0,max(yValues[:-1]))

plt.scatter(xValues, yValues)

# uncomment following to show estimated line fit in orange:-
plt.plot(xValues, mEst*xValues + cEst, color='orange')
plt.xlim(0,60)
plt.ylim(0,100)
plt.grid()
plt.savefig('fig-4.jpeg')
plt.show()