#!/usr/bin/python3
import sys

# Function description:
# This function calculates the factorial of a given number 'n' recursively.
# The factorial of a number n (denoted n!) is the product of all positive integers less than or equal to n.
# Example: factorial(5) = 5 * 4 * 3 * 2 * 1 = 120

# Parameters:
# n (int): A non-negative integer for which we want to calculate the factorial.
# The value of n should be an integer greater than or equal to 0.

# Returns:
# int: The factorial of the input number 'n'.
# If n is 0, it returns 1, as 0! = 1 by definition.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read the input number from the command-line argument, calculate its factorial, and print the result.
f = factorial(int(sys.argv[1]))
print(f)
