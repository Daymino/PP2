import re

# Define the file name
file_name = "row.txt"

# Open the file for reading
with open(file_name, 'r', encoding='utf-8') as file:
    # Read each line in the file
    for line in file:
        # Use regex to convert camel case to snake case
        snake_case = re.sub(r'([a-zа-я])([A-ZА-Я])', r'\1_\2', line)
        
        # Print the snake case string
        print(snake_case.lower().strip())