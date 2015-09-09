__author__ = 'zhengyangqiao'

import matplotlib.pyplot as plt

## Normal line plot
x = [1,2,3]
y = [5,7,4]

x2 = [1,2,3]
y2 = [10,14,12]

plt.figure(0)
plt.plot(x, y, label = 'First line')
plt.plot(x2, y2, label = 'Second line')

plt.xlabel('Plot number')
plt.ylabel('Important var')

plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()

## Histograms plot
plt.figure(1)
plt.bar([1,7,10],[2,8,1], label="Example one")

plt.bar([2,4,6],[8,2,5], label="Example two", color='g')
plt.legend()
plt.xlabel('bar number')
plt.ylabel('bar height')

plt.title('Epic Graph\nAnother Line! Whoa')

plt.show()

## Scatter plot
x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

plt.figure(2)
plt.scatter(x,y, label='skitscat', color='k', s=25, marker="o")

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()

## Scatter plot
days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating =   [2,3,4,3,2]
working =  [7,8,7,2,2]
playing =  [8,5,7,8,13]

plt.figure(3)
plt.plot([],[],color='m', label='Sleeping', linewidth=5)
plt.plot([],[],color='c', label='Eating', linewidth=5)
plt.plot([],[],color='r', label='Working', linewidth=5)
plt.plot([],[],color='k', label='Playing', linewidth=5)

plt.stackplot(days, sleeping,eating,working,playing, colors=['m','c','r','k'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.show()