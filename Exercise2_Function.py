# Write a function that prints all factors of the given parameter x
def print_factor(x):
    # your code here
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)

print_factor(12)

print_factor(52633)
