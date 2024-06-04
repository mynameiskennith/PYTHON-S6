import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([1,3,2,5,4])

# To subtract two arrays
print(f'Difference = {np.subtract(a,b)}')

# To multiply two arrays
print(f'Product = {np.multiply(a,b)}')

# To divide arrays
print(f'Quotient = {np.divide(a,b)}')

# To find remainder
print(f'Remainder = {np.remainder(a,b)}')

# To find Mod
print(f'Mod = {np.mod(a,b)}')

# To find the power
print(f'a powered b = {np.power(a,b)}')