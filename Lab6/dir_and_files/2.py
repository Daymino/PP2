import os

def check_path_access(path):
    # Check for path existence
    if not os.path.exists(path):
        print(f"The path '{path}' does not exist.")
        return

    # Check for readability
    if os.access(path, os.R_OK):
        print(f"The path '{path}' is readable.")
    else:
        print(f"The path '{path}' is not readable.")

    # Check for writability
    if os.access(path, os.W_OK):
        print(f"The path '{path}' is writable.")
    else:
        print(f"The path '{path}' is not writable.")

    # Check for executability
    if os.access(path, os.X_OK):
        print(f"The path '{path}' is executable.")
    else:
        print(f"The path '{path}' is not executable.")

# Example usage:
specified_path = "C:\\Users\giper\OneDrive\Desktop\KBTU_2S" 

# C:\\Users\giper\OneDrive\Desktop\KBTU_2S\PP_2\Lab_6\Python

# C:\\Users\giper\OneDrive\Desktop\KBTU_2S

check_path_access(specified_path)