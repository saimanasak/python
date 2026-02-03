n = int(input("Enter a number: "))

# Square root of the number
p = n ** 0.5

# Product of the square root
r = p * p

# Compare the values
if n == r:
    print("A perfect square")
else:
    print("Not a perfect square")