with open('file1.txt','w+') as f:
    f.write('qwerty is gud')
with open('file1.txt','r') as f:
    print(f.read())

listt = ['assss','www','qwe','tyui']
with open('file2.txt','w') as f2:
    for i in listt:
        f2.write(i+'\n')