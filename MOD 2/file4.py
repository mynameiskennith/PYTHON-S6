nums = list(map(int,input('Enter the numbers : ').split()))

fo = open('odd.txt','w')
fe = open('even.txt','w')

for i in nums:
    if i%2==0:
        fe.write(f'{i} ')
    else:
        fo.write(f'{i} ')

fe.close()
fo.close()