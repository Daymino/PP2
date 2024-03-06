import os

def analyze_path(input_path):
    # Check if the path exists
    if os.path.exists(input_path):
        print(f"The path '{input_path}' exists.")

        # Extract the filename and directory portions
        filename = os.path.basename(input_path)
        directory = os.path.dirname(input_path)

        print(f"Filename: {filename}")
        print(f"Directory: {directory}")
    else:
        print(f"The path '{input_path}' does not exist.")

# Example usage:
given_path = "C:\\Users\giper\OneDrive\Desktop\KBTU_2S\PP_2\Lab_6\Python\just_a_file.txt"

# C:\\Users\giper\OneDrive\Desktop\KBTU_2S\PP_2\Lab_6\Python\dir_and_files\3.py
 
analyze_path(given_path)