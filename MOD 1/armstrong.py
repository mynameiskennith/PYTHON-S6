a = input('Enter a number : ')
arm = 0

for i in a:
    arm+=int(i)**3

print(f'{a} is {'Armstrong' if arm==int(a) else 'not an Armstrong'}')