import re

def snake_to_camel(snake_case):
    return re.sub(r'_([a-zа-я])', lambda x: x.group(1).upper(), snake_case)

# Define the file name
file_name = "row.txt"

# Open the file for reading
with open(file_name, 'r', encoding='utf-8') as file:
    # Read each line in the file
    for line in file:
        # Use regex to find snake case strings and convert to camel case
        modified_line = re.sub(r'\b[a-zа-я]+(?:_[a-zа-я]+)*\b', lambda x: snake_to_camel(x.group()), line)
        
        # Print the modified line
        print(modified_line.strip())