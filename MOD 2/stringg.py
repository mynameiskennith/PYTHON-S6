message = 'python is awsome isn\'t it?'

print(f'The number of occurances of  p is {message.count('p')}')
print(f'o from 1 to 20 {message.count('o',1,20)}')
print(f'message ends with n - {message.endswith('n')}')
print(f'1st occurance of is {message.find('is')}')
print(f'The last occurance of is is {message.rfind('z')}')
print(message.center(5,'y'))