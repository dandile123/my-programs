import sys

# Check command line arguments
if len(sys.argv) != 3:
    print("Usage: python comparefiles.py <file1> <file2>")
    exit()

file1 = sys.argv[1]
file2 = sys.argv[2]

try:
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        if f1.read() == f2.read():
            print("Success")
        else:
            print("Failure")

except FileNotFoundError:
    print("One or both files do not exist.")
