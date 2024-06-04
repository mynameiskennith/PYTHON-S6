l = list(map(int,input('Enter the elements for the list : ').split()))

lodd = [i for i in l if i%2!=0]
leven = [i for i in l if i%2==0]

print(f'Even List : {leven} \nOdd List : {lodd}')