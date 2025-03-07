def rfs(fp):
    try:
        with open(fp, 'r') as file:
            for f in file:
                print(f, end='')
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)
rfs("text1.txt")