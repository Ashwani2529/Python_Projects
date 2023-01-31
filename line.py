import numpy as np
import matplotlib.pyplot as plt

#define data
x = np.array([1, 2, 3, 4, 5, 6, 7, 8,9])
y = np.array([2, 5, 6, 7, 9, 12, 16, 19,21])

#find line of best fit
a, b = np.polyfit(x, y, 1)

#add points to plot
plt.scatter(x, y, color='green')

#add line of best fit to plot
plt.plot(x, a*x+b, color='red', linestyle='dashed', linewidth=1.1)

#add fitted regression equation to plot
plt.text(1, 17, 'y = ' + '{:.2f}'.format(b) + ' + {:.2f}'.format(a) + 'x', size=14)
