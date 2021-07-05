import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


y = [0.143,0.167,0.095,0.119,0]
x = [0.051,0.038,0.077,0.064,0.128]
y1=[0.190,0.167,0,0.048,0.095]
x1=[0.026,0.038,0.128,0.103,0.077]
plt.plot(x, y, 'r-o',label='A')
plt.plot(x1, y1, 'g-o',label='B')
plt.legend()
plt.xlabel('1-Specificity')
plt.ylabel('Sensitivity')
plt.title('the curve of Sensitivity vs. (1- Specificity)')

plt.show()