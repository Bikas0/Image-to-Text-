import os

def remove_spaces(directory):
    # Get list of files in the directory
    files = os.listdir(directory)

    # Iterate over each file
    for file in files:
        if " " in file:  # Check if file name contains space
            # Construct new file name by replacing spaces with underscores
            new_name = file.replace(" ", "_")
            # Get full path of the file
            old_path = os.path.join(directory, file)
            new_path = os.path.join(directory, new_name)
            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed {file} to {new_name}")

# Replace 'directory_path' with the path to your image folder
directory_path = 'Datasets/captcha_images_v2'
remove_spaces(directory_path)
