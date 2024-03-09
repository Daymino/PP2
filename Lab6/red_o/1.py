import os
import time

folder_name_prefix = "red_o"
project_path = os.getcwd()

counter = 1

while True:
    folder_name = f"{folder_name_prefix}_{counter}"
    folder_path = os.path.join(project_path, folder_name)

    os.makedirs(folder_path, exist_ok=True)
    print(f"Создана папка: {folder_path}")

    time.sleep(1)
    counter+=1