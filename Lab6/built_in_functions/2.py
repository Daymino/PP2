def count_upper_lower(string):
    # Initialize counters for upper and lower case letters
    upper_count = 0
    lower_count = 0

    # Iterate through each character in the string
    for char in string:
        # Check if the character is an uppercase letter
        if char.isupper():
            upper_count += 1
        # Check if the character is a lowercase letter
        elif char.islower():
            lower_count += 1

    # Print the results
    print(f"Number of uppercase letters: {upper_count}")
    print(f"Number of lowercase letters: {lower_count}")

# Example usage:
input_string = str(input())
count_upper_lower(input_string)