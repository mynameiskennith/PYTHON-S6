import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('p1.csv')

df.plot(kind = 'scatter',x='hh',y='jj')
plt.title('p1.csv')
plt.show()
