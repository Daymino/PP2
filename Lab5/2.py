import re

# Define the file name
file_name = "row.txt"

# Open the file for reading
with open(file_name, 'r', encoding='utf-8') as file:
    # Read each line in the file
    for line in file:
        # Use regex to find the pattern 'a' followed by two to three 'b's
        if re.search(r'ab{2,3}', line):
            # Print the matching line
            print(line.strip())