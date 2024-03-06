def is_palindrome(input_str):
    # Convert the input string to lowercase to make the comparison case-insensitive
    cleaned_str = input_str.lower()

    # Remove non-alphanumeric characters from the string
    cleaned_str = ''.join(char for char in cleaned_str if char.isalnum())

    # Check if the cleaned string is equal to its reverse
    return cleaned_str == cleaned_str[::-1]

# Example usage:
input_string = str(input()) # A man, a plan, a canal, Panama!
result = is_palindrome(input_string)

if result:
    print(f"The string '{input_string}' is a palindrome.")
else:
    print(f"The string '{input_string}' is not a palindrome.")