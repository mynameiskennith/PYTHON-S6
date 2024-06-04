name = input('Enter your name : ')
roll = input('Enter your roll no : ')

with open(name+'.txt','w') as f:
    f.write(f'Name : {name}\nRoll No : {roll}')

cls = input('Enter your class : ')
reg = input('Enter your reister number : ')
with open(name+'.txt','a') as f:
    f.write(f'Class : {cls}\nRegister No : {reg}')