import os
import sys
from Logger import CreateLog
import logging

def DirectoryFileSearch(dirname, extension):
    if not os.path.isdir(dirname):
        logging.error("Invalid directory")
        return

    for file in os.listdir(dirname):
        if file.endswith(extension):
            logging.info(file)

def main():
    CreateLog("FileSearch.log")

    if len(sys.argv) != 3:
        logging.error("Invalid arguments")
        return

    DirectoryFileSearch(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
