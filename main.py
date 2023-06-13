import os
import sys
from os.path import join


def generate_file_tree(root_dir, exclude_dirs=None, indent="", output_file=None):
    files = os.listdir(root_dir)

    output_file.write(
        f"{indent}{os.path.basename(root_dir)}/\n"
    )  # Print the root directory

    for file in files:
        file_path = join(root_dir, file)
        if os.path.isdir(file_path):
            if exclude_dirs is not None and file in exclude_dirs:
                continue
            output_file.write(f"{indent}|  |- {file}/\n")
            generate_file_tree(file_path, exclude_dirs, indent + "|  ", output_file)
        else:
            output_file.write(f"{indent}|  |- {file}\n")


# Check if the root directory path is provided as a command line argument
if len(sys.argv) > 1:
    root_directory = sys.argv[1]
else:
    print("Please provide the root directory path as a command line argument.")
    sys.exit(1)

exclude_directories = [
    ".git",
    ".gitignore",
]  # Add the directories you want to exclude to this list
output_path = "file_tree.txt"  # Output file path

with open(output_path, "w") as output_file:
    generate_file_tree(root_directory, exclude_directories, output_file=output_file)

print(f"File tree generated and saved to {output_path}.")
