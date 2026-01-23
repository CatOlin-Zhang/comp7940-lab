# Write a program to find all factors of the numbers in the list l
l = [52633, 8137, 1024, 999]

# your code here
def print_factors(x):
    """Print all factors of x"""
    factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
    return factors

# Find and print factors for each number in the list
for number in l:
    factors = print_factors(number)
    print(f"Factors of {number}: {factors}")