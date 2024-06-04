import matplotlib.pyplot as plt
import numpy as np

x = np.array(["S","A+","A","B+","B"])
y = np.array([12,21,43,21,22])

plt.bar(x,y,color="r")

plt.show()