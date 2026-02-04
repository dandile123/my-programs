filename = input("Enter file name: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("File Contents:\n")
        print(content)
except FileNotFoundError:
    print(f"{filename} does not exist.")
