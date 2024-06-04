import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(1,4))
x = np.array([25,23,11,55])

#labels of the pie chart
labels = ['A','B','C','D']

plt.pie(x, labels=labels)
plt.show()