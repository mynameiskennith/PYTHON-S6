import matplotlib.pyplot as plt
import numpy as np

x = np.array(["S","A+","A","B+"])
y = np.array([32,22,55,1])

plt.barh(x,y)
plt.show()