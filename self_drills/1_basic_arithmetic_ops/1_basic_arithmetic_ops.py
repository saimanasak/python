# Input prompt for the two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Addition, Subtraction, Product
sum = num1 + num2
difference = num1 - num2
product = num1 * num2


print("Sum: ", sum)
print("Difference: ", difference)
print("Product: ", product)

# Handle division by zero
if num2 != 0:
    quotient = num1 // num2
    remainder = num1 % num2
    print("Quotient: ", quotient)
    print("Remainder: ", remainder)
else:
    print("Division by zero is not allowed.")