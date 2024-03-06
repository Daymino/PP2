import re

# Define the file name
file_name = "row.txt"

# Open the file for reading
with open(file_name, 'r', encoding='utf-8') as file:
    # Read each line in the file
    for line in file:
        # Use regex to insert spaces between words starting with capital letters
        modified_line = re.sub(r'(?<=[a-zа-я])([A-ZА-Я])', r' \1', line)
        
        # Print the modified line
        print(modified_line.strip())