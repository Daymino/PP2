def copy_file(source_path, destination_path):
    try:
        with open(source_path, 'r') as source_file:
            content = source_file.read()

        with open(destination_path, 'w') as destination_file:
            destination_file.write(content)

        print("File copied successfully.")
    except FileNotFoundError:
        print(f"Source file '{source_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
source_file_path = "C:\\Users\giper\OneDrive\Desktop\KBTU_2S\PP_2\Lab_6\Python\dir_and_files\source.txt"        
destination_file_path = "C:\\Users\giper\OneDrive\Desktop\KBTU_2S\PP_2\Lab_6\Python\dir_and_files\output.txt"  

copy_file(source_file_path, destination_file_path)