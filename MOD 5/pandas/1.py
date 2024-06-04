import pandas as pd

my_dict ={
    'name' : ["a","b","c","d"],
    'age': [20,12,34,21],
    'designation' : ["Vp","VVP",'Cheif','Omen']
}

df = pd.DataFrame(my_dict, index=[1,2,3,4])

df.to_csv('p1.csv')
df.to_csv('p2.csv', index=False)
print(df)