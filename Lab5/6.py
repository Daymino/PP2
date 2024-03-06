import re

# Define the file name
file_name = "row.txt"

# Open the file for reading
with open(file_name, 'r', encoding='utf-8') as file:
    # Read each line in the file
    for line in file:
        # Use regex to replace space, comma, or dot with a colon
        modified_line = re.sub(r'[ ,.]', ':', line)
        
        # Print the modified line
        print(modified_line.strip())