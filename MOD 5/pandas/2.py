import pandas as pd

ll = {
    'Reg No.' : ['ABC123','ECH256','FET345','GMT734'],
    'Name' : ['Ganesh Kumar','John Mathew','Reena K','Adil M'],
    'Semester' : ['S8','S7','S6','S5'],
    'College' : ['ABC','ECH','FET','GMT'],
    'CGPA' : [9.8,9.9,9.7,9.75]
}

df = pd.DataFrame(ll)
df.to_csv('PandasUQ.csv',index=False)

print(df)