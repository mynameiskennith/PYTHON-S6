import pandas as pd

use = ['name','age']

employee = pd.read_csv('p1.csv',usecols=use)
print(employee.head())

print(employee.tail())