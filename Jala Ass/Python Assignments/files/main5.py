def reading_index(fp, p, l):
    try:
        with open(fp, 'r') as file:
            file.seek(p)
            print(file.read(l))
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)
reading_index("text1.txt", 10, 20)