import os

def generate_files(folder_path):
    try:
        # Ensure the folder exists, create it if not
        os.makedirs(folder_path, exist_ok=True)

        # Generate files A.txt to Z.txt
        for char in range(ord('A'), ord('Z') + 1):
            file_name = f"{chr(char)}.txt"
            file_path = os.path.join(folder_path, file_name)

            with open(file_path, 'w') as file:
                file.write("Just a txt-file")

        print("Files generated successfully in the folder")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
output_folder = "C:\\Users\giper\OneDrive\Desktop\KBTU_2S\PP_2\Lab_6\Python\dir_and_files\proverka"  
generate_files(output_folder)