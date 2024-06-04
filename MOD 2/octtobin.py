oct = input('Enter the octal value')
binn = ''
print(int(oct,8))
for i in oct:
    binn = binn + bin(int(i))[2:]
print(binn)