import matplotlib.pyplot as plt
import numpy as np

x = np.array(["S","A+","A","B+"])
y = np.array([12,27,20,10])

plt.title('Python Programming')
plt.ylabel('No of students')
plt.xlabel('Grade')

plt.bar(x,y)

plt.show()