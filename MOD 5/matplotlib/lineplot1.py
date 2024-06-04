import matplotlib.pyplot as plt

years = [2000,2001,2002,2003,2004,2005]
runs = [100,23,45,11,200,100]
runz = [105,30,45,11,200,100]
plt.title('Progress Grid')
plt.plot(years,runz,'b-o')
plt.plot(years,runs,'r-x')

plt.show()