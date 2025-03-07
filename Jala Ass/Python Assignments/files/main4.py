with open("sample.txt", "rb") as file:
    file.seek(10)
    content = file.read(20)
    print(content.decode())
