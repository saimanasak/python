f = float(input("Enter a number, float: "))

# Get integer
integer = int(f)

# Get fractional part
decimal = f - int(f)

# Remove precision error
decimal = round(decimal, 10)

print("Extracted integer = ", integer)
print("Extracted decimal = ", decimal)