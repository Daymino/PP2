import re

# Define the file name
file_name = "row.txt"

# Open the file for reading
with open(file_name, 'r', encoding='utf-8') as file:
    # Read each line in the file
    for line in file:
        # Use regex to split the line at uppercase letters
        split_parts = re.split(r'([A-ZА-Я])', line)
        
        # Remove empty strings from the result
        split_parts = list(filter(None, split_parts))
        
        # Print the split parts
        print(split_parts)