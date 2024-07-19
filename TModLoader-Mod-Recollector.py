import os
import shutil
from datetime import datetime

def get_latest_date_folder(path):
    # List all directories in the given path
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    # Parse the directories assuming they are in the format 'year.month'
    latest_folder = max(dirs, key=lambda x: datetime.strptime(x, "%Y.%m"))
    return latest_folder

def copy_tmod_files(source_base_path, dest_path):
    # Iterate over all folders in the source base path
    for root_dir in os.listdir(source_base_path):
        full_dir_path = os.path.join(source_base_path, root_dir)
        if os.path.isdir(full_dir_path):
            # Get the latest date folder
            latest_folder = get_latest_date_folder(full_dir_path)
            latest_folder_path = os.path.join(full_dir_path, latest_folder)
            # Search for .tmod files and copy each one
            for file in os.listdir(latest_folder_path):
                if file.endswith('.tmod'):
                    src_file_path = os.path.join(latest_folder_path, file)
                    shutil.copy(src_file_path, dest_path)
                    print(f"Copied {file} to {dest_path}")

# Set the base paths
source_base_path = r"C:\Program Files (x86)\Steam\steamapps\workshop\content\1281930"
destination_path = r"C:\Users\T\Downloads\mods"

# Ensure the destination directory exists
os.makedirs(destination_path, exist_ok=True)

# Copy the tmod files
copy_tmod_files(source_base_path, destination_path)
