import os
import subprocess
import sys
from pathlib import Path

__version__ = "0.1.9"

save_folder = Path.home() / "Downloads"


def open_file(file_path):
    """Open a file with the system's default application."""
    if sys.platform.startswith("win"):
        os.startfile(file_path)
    elif sys.platform == "darwin":
        subprocess.run(["open", file_path], check=True)
    else:
        subprocess.run(["xdg-open", file_path], check=True)


def list_directories(path):
    if not os.path.isdir(path):
        print(f"The specified path ({path}) is not a directory.")
        return

    try:
        directory_names = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
    except OSError as error:
        print(f"Could not read the folder ({path}): {error}")
        return

    output_file_path = os.path.join(save_folder, "directory_names.txt")

    if os.path.exists(output_file_path):
        overwrite = input(f"{output_file_path} already exists. Overwrite it? Y/N ")
        if overwrite.strip().lower() != "y":
            print("Nothing was written.")
            return

    try:
        save_folder.mkdir(parents=True, exist_ok=True)
        with open(output_file_path, 'w', encoding='utf-8') as file:
            for directory in sorted(directory_names, key=str.lower):
                file.write(directory + '\n')
    except OSError as error:
        print(f"Could not write the output file ({output_file_path}): {error}")
        return

    print(f"Folder names were saved in {output_file_path}")
    continue_prompt = input("Do you want to open the file? (Y/N) ")
    if continue_prompt.strip().lower() == "y":
        print("Opening directory_names.txt")
        try:
            open_file(output_file_path)
        except (OSError, subprocess.CalledProcessError) as error:
            print(f"Could not open the file automatically: {error}")


if __name__ == "__main__":
    user_path = input("Enter the folder path to list its subfolders: ")
    list_directories(user_path)
