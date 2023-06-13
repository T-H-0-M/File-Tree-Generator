# File Tree Generator

This Python script generates a file tree for a given root directory. The file tree is printed to the console and saved to a text file.

## Prerequisites

- Python 3.x

## Usage

1. Provide the root directory path as a command-line argument when running the script. For example:

```bash
python main.py /path/to/root_directory
```

2. The script will generate a file tree for the specified root directory, excluding any directories listed in the `exclude_directories` list.

3. The file tree will be printed to the console, and the complete file tree will be saved to a text file named `file_tree.txt` in the current directory.

## Customization

You can customize the behavior of the script by modifying the following variables:

- `exclude_directories`: This is a list of directories that you want to exclude from the file tree generation. By default, it includes ".git" and ".gitignore".

- `output_path`: This is the file path where the generated file tree will be saved. By default, it is set to "file_tree.txt".

## Example

Suppose you want to generate a file tree for the root directory "/path/to/project". You would run the script as follows:

```bash
python file_tree_generator.py /path/to/project
```

The script will generate the file tree for the specified root directory, excluding any directories listed in `exclude_directories`. The file tree will be printed to the console and saved to "file_tree.txt" in the current directory.

## References

- [Python Documentation](https://www.python.org/doc/)
- [os Module Documentation](https://docs.python.org/3/library/os.html)
- [sys Module Documentation](https://docs.python.org/3/library/sys.html)
- [Create a Python Directory Tree Generator](https://www.javatpoint.com/create-a-python-directory-tree-generator)
- [List directory tree structure in Python](https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python)
- [ChatGPT](https://openai.com/blog/chatgpt/)
