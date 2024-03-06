import os

def delete_file(file_path):
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            print(f"The file does not exist.")
            return

        # Check for file access
        if not os.access(file_path, os.W_OK):
            print(f"You don't have write access to the file. Deletion aborted.")
            return

        # Delete the file
        os.remove(file_path)
        print(f"File deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
specified_file_path = r"C:\\Users\giper\OneDrive\Desktop\KBTU_2S\PP_2\Lab_6\Python\dir_and_files\delete.txt"  
delete_file(specified_file_path)