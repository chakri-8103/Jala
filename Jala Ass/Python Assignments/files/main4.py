def rfar(fp, p):
    try:
        with open(fp, 'r') as file:
            file.seek(p)
            print(file.read())
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)
rfar("text1.txt",10)