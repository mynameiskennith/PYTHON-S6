import math
n =10

for i in range(2,int(math.sqrt(n))+1,1):
    if n%i==0:
        print('not prime')
        break
print('It is prime')