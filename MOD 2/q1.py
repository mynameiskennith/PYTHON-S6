def summ(n):
    if n==0:
        return 0
    else:
        return n+summ(n-1)

print(summ(10))