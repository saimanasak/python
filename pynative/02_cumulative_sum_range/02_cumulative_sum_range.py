# Print the heading
print("Printing current and previous number sum in a range(10)")

# Initialize the previous number
previous = 0

# Iterate through numbers from 0 to 9
for current in range(10):

    # Handle the first iteration
    if current == 0:
        current = previous = 0
        total = 0
        print("Current Number", current, "Previous Number", previous, "Sum:", total)

    else:
        # Calculate the sum
        total = current + previous

        # Print the result
        print("Current Number", current, "Previous Number", previous, "Sum:", total)

        # Save the current number for the next iteration
        previous = current