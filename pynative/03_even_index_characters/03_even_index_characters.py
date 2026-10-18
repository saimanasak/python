# Get a string from the user
word = input("Enter a word: ")

# Get the length of the string
length = len(word)

# Iterate through even index positions
for i in range(0, length, 2):
    print(word[i])

# Alternative approach using string slicing:
# for char in word[::2]:
#     print(char)