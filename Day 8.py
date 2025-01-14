# day 8
"""
topics covered-
1. modules and packages
"""
# importing modules from packages

from my_package import sample_arithmetic
print(sample_arithmetic.sum(1,2))

from my_package2 import sample_factorial
print(sample_factorial.factorial(5))

from my_package import sample_comparator
print (sample_comparator.greatest(1, 2, 3, 4, 5, 6, 7, 10))
print (sample_comparator.least(1, 2, 3, 4, 5, 6, 7, 10))

from my_package import sample_calculator
result = sample_calculator.calculator()
print(f"Final result: {result}")

from my_package2 import sample_prime
print(sample_prime.prime(7))
