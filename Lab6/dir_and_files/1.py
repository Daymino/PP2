import os

def list_directories(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    return directories

def list_files(path):
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return files

def list_all(path):
    all_items = os.listdir(path)
    return all_items

# Example usage:
specified_path = "C:\\Users\giper\OneDrive\Desktop\KBTU_2S\PP_2\Lab_6\Python"

# C:\\Users\giper\OneDrive\Desktop\KBTU_2S\PP_2\Lab_6\Python

# C:\\Users\giper\OneDrive\Desktop\KBTU_2S

directories_list = list_directories(specified_path)
files_list = list_files(specified_path)
all_items_list = list_all(specified_path)

print("Directories:", directories_list)
print("Files:", files_list)
print("All Directories and Files:", all_items_list)