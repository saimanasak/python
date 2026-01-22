num = int(input("Enter a number to check: "))

float_result = num / 2
int_result = num //2

if float_result == int_result:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")