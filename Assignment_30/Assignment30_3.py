filename = input("Enter file name: ")

try:
    with open(filename, 'r') as file:
        for line in file:
            print(line, end='')

except FileNotFoundError:
    print("File does not exist.")
