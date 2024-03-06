import re

# Define the file name
file_name = "row.txt"

# Open the file for reading
with open(file_name, 'r', encoding='utf-8') as file:
    # Read each line in the file
    for line in file:
        # Use regex to find sequences of lowercase letters joined with an underscore
        matches = re.findall(r'\b[a-zа-я]_[a-zа-я]+\b', line)
        
        # Print the matching sequences
        for match in matches:
            print(match)