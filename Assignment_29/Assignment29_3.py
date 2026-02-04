import sys

# Check command line arguments
if len(sys.argv) != 2:
    print("Usage: python copyfile.py <source_file>")
    exit()

source_file = sys.argv[1]
destination_file = "Demo.txt"

try:
    with open(source_file, 'r') as src:
        data = src.read()

    with open(destination_file, 'w') as dest:
        dest.write(data)

    print("File copied successfully into Demo.txt")

except FileNotFoundError:
    print("Source file does not exist.")
