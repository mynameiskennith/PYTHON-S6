t = int(input('Enter the time in seconds : '))

s = t%60
m = t//60
h = m//60
m = t%60

print(f'HH:MM:SS = {h}:{m}:{s}')