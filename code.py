import os

import shutil


def intialize_folder(folder_path):
    print("*"*15 ,"AUTOMATED FOLDER CLEANER ACTIVATED", "*"*15, "\n")

    if os.path.exists(folder_path):
        
        folder_items = os.listdir(folder_path)

        print(f"Total items in the folder is: {len(folder_items)}")
        print(f"The items in the file are as follows:\n", folder_items)

        folder = []
        files = []

        for items in folder_items:
            name, extension = os.path.splitext(items)
            
            if extension == "":
                folder.append(items)
            elif extension != "":
                files.append(items)

        all_extensions = []

        for file_name in files:
            name, extension = os.path.splitext(file_name)
            all_extensions.append(extension)

        unique_extension = set(all_extensions)

        for ext in unique_extension:
            folder_name  = ext.replace(".","")

            new_folder_path = os.path.join(folder_path, folder_name)

            os.makedirs(new_folder_path, exist_ok=True)

        print(f"\nFolders detected: {folder}")
        print(f"Files detected: {files}")

        for file in files:
            source_path = os.path.join(folder_path, file)

            _, file_extension = os.path.splitext(file)

            file_extension = file_extension.replace(".","")

            destination_path = os.path.join(folder_path, file_extension)

            shutil.move(source_path, destination_path)
    
    else:
        print("The given path file doesn't exists")


target_dir = input("Please provide the folder paths to be cleaned (separated by commas): ")
temp_dir = list(target_dir.split(","))

for file_paths in temp_dir:
    clean_path = file_paths.strip()

    intialize_folder(clean_path)