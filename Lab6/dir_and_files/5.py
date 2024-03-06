def write_list_to_file(file_path, my_list):
    try:
        with open(file_path, 'w') as file:
            for item in my_list:
                file.write(str(item) + '\n')
        print(f"List written to the file '{file_path}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
file_path = "C:\\Users\giper\OneDrive\Desktop\KBTU_2S\PP_2\Lab_6\Python\just_a_file.txt" 
my_list = [1, 2, 3, 4, 5]

write_list_to_file(file_path, my_list)