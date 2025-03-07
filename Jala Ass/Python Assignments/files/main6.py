import os

file_path = "sample.txt"

if os.access(file_path, os.R_OK):
    print("File has read access")
else:
    print("File does not have read access")

if os.access(file_path, os.W_OK):
    print("File has write access")
else:
    print("File does not have write access")
