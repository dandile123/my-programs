filename = input("Enter file name: ")
search_word = input("Enter word to search: ")

try:
    with open(filename, 'r') as file:
        content = file.read()

        if search_word in content:
            print("Word is present in the file.")
        else:
            print("Word is not present in the file.")

except FileNotFoundError:
    print("File does not exist.")
