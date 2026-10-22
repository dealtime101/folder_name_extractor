import os
import subprocess
import sys
from pathlib import Path

__version__ = "0.1.3"

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

    directory_names = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]

    save_folder.mkdir(parents=True, exist_ok=True)
    output_file_path = os.path.join(save_folder, "directory_names.txt")

    with open(output_file_path, 'w') as file:
        for directory in directory_names:
            file.write(directory + '\n')

    print(f"Folder names were saved in {output_file_path}")
    continue_prompt = input(f"Do you want to open the file? Y/N")
    if continue_prompt.strip().lower() == "y":
        print("Opening directory_names.txt")
        try:
            open_file(output_file_path)
        except (OSError, subprocess.CalledProcessError) as error:
            print(f"Could not open the file automatically: {error}")
    else:
        return


if __name__ == "__main__":
    user_path = input("Enter the folder path to list its subfolders: ")
    list_directories(user_path)
