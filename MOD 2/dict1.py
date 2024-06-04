a = list(input('Enter : '))
dict={}
for i in a:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(f'Counts :')
for i in dict.keys():
    print(f'{i} : {dict[i]}')