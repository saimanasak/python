n = int(input("Enter a number: "))

if (n % 3 == 0) and (n % 5 == 0):
    print(n, "is divisible by both 3 and 5.")
else:
    print(n, "isn't divisible by 3 and 5.")