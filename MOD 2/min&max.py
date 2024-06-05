def min_max(l):
    return min(l),max(l)

list1 = list(map(int,input('Enter the list : ').split()))
min,max = min_max(list1)
print(f'Minimum is {min}\nMaximum is {max}')