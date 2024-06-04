def factors(x):
    print(f'Factors of {x} are : ',end='')
    for i in range(1,x+1):
        if x%i==0:
            print(i, end=', ')

factors(567)