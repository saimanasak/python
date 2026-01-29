f = input("Enter a float: ")
n = int(input("Enter an integer: "))

# Convert float to integer without losing precision
s1 = f.split('.')
final_int = int("".join(s1))

# Convert integer to float
final_float = float(n)

# Convert integer to complex
final_comp = complex(n)

print(final_int)
print(final_float)
print(final_comp)