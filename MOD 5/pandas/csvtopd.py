import pandas as pd

employee = pd.read_csv("p2.csv", index_col=0)

print(employee.head())