import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(270,50,250)
print(x)
plt.hist(x)
plt.show()