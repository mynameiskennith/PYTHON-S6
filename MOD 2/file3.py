f = open('integers.txt', 'w')
num = list(map(int, input('Enter the numbers: ').split()))
f.writelines(f"{n} " for n in num)
f.close()

f = open('integers.txt', 'r')
summ = sum(map(int, f.read().split()))
print(summ)
f.close()