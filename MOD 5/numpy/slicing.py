import numpy as np

arr = np.array([0,1,2,3,4,5,6,7,8,9,10])
print(arr[1:5])

# giving the beginning
print(arr[4:])

# print until the given ending
print(arr[:4])

# print from the end
print(arr[:-1])
print(arr[-3:-1])

print(arr[1:5:2])