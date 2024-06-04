l = input('Enter the values for the list : ').split()

print(f'The list in reverse order : {l[::-1]}')

w = input('Enter the word you want to check the occurance : ')
print(f'The occurance of {w} is {l.count(w)} times')