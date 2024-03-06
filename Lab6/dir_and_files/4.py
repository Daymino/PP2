def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
            return line_count
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
file_path = "C:\\Users\giper\OneDrive\Desktop\KBTU_2S\PP_2\Lab_4\JSON\sample-data.json"  
lines_count = count_lines(file_path)

if lines_count is not None:
    print(f"The number of lines is: {lines_count}")