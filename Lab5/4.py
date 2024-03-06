import re

# Define the file name
file_name = "row.txt"

# Open the file for reading
with open(file_name, 'r', encoding='utf-8') as file:
    # Read each line in the file
    for line in file:
        # Use regex to find sequences of one upper case letter followed by lower case letters
        matches = re.findall(r'\b[A-ZА-Я][a-zа-я]+\b', line)
        
        # Print the matching sequences
        for match in matches:
            print(match)