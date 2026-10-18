# Get two integers from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate the product and sum
p = num1 * num2
s = num1 + num2

# Print the product if it is <= 1000, else print the sum
if p <= 1000:
    print("Result:", p)
else:
    print("Result:", s)