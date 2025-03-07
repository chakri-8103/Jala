def read_file(file_path):
    try:
        with open(file_path) as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found.")
read_file("text.txt")
