# TModLoader-Mod-Recollector

This Python script helps streamline the process of setting up Terraria dedicated servers by copying the most recent .tmod files from TModLoader mod directories into a single folder.
It's designed to simplify server preparation by consolidating mods that are typically scattered across different directories.

## Features

- **Automates the Copying of Mod Files:** Finds and copies the latest .tmod files from multiple directories based on the most recent dates.
- **Date-Based File Selection:** Identifies the latest mods by looking at folder dates formatted as 'year.month'.
- **Consolidates Mods into a Single Folder:** Gathers all relevant .tmod files in one location for easy access.

## Requirements

- Python 3.x
- Libraries: `os`, `shutil`
- Proper access to the file system where the mods are stored.

## Setup

1. **Install Python:**
   - Python 3.x is required and can be installed from [python.org](https://www.python.org/).

2. **Configure the Script:**
   - Modify `source_base_path` to point to your mods' base directory.
   - Set `destination_path` to where you want the consolidated mods to be placed.

## Usage Instructions

1. **Prepare Directories:**
   - Ensure the paths in `source_base_path` and `destination_path` are correctly set according to your server setup.

2. **Execute the Script:**
   - Run the script using:
     ```bash
     python tmodloader_mod_recollector.py
     ```

3. **Check Results:**
   - The script outputs the names of copied mods. Verify these in the destination folder to confirm correct copying.

4. **Use in Server Setup:**
   - Use the consolidated folder for setting up your Terraria server.
