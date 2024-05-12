from random import randint
from math import isqrt

#  Use random module, randint() to generate a random number in the range (1, 100).
random_number = randint(1, 100)
# Use math module, isqrt() to round a square root number downwards to the nearest integer.
sqrt = isqrt(random_number)

# Print out the result.
print(f'Square root of {random_number} = {sqrt}')