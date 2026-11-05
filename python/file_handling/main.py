import os

path=input ("Enter the path of the file: ")
path=path.strip("'").strip('"')

files=0
dirs=0
try:
    if not os.path.exists(path):
        raise FileNotFoundError(f"The specified path {path} does not exist.")
    if not os.path.isdir(path):
        raise NotADirectoryError(f"The specified path {path} is not a directory.")

    for root, directories, filenames in os.walk(path):
        for directory in directories:
            dirs += 1
        for filename in filenames:
            files += 1
    print(f"Total number of files: {files}")
    print(f"Total number of directories: {dirs}")
except FileNotFoundError as e:
    print(f"Error: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
except PermissionError as e:
    print(f"Permission denied: {e}")
