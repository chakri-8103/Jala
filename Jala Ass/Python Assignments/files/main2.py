def wtf(file_path):
    try:
        text = input("Enter text to write to file: ")
        with open(file_path, 'w') as file:
            file.write(text)
        print("Text written to file successfully.")
    except Exception as e:
        print("An error occurred:", e)
wtf("text1.txt")