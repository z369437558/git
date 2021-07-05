import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


y = [0.6, 0.7, 0.4, 0.5, 0]
x = [0.143, 0.167, 0.095, 0.119, 0]
y1=[0.8, 0.7, 0, 0.2, 0.4]
x1=[0.190, 0.167, 0, 0.048, 0.095]
plt.plot(x, y, 'r-o',label='A')
plt.plot(x1, y1, 'g-o',label='B')
plt.legend()
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('precision-recall curves')

plt.show()