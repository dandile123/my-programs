import os
import sys
from Logger import CreateLog
import logging

def DirectoryRename(dirname, old_ext, new_ext):
    if not os.path.isdir(dirname):
        logging.error("Invalid directory")
        return

    for file in os.listdir(dirname):
        if file.endswith(old_ext):
            old_path = os.path.join(dirname, file)
            new_path = os.path.join(dirname, file.replace(old_ext, new_ext))
            os.rename(old_path, new_path)
            logging.info(f"Renamed {file}")

def main():
    CreateLog("Rename.log")

    if len(sys.argv) != 4:
        logging.error("Invalid arguments")
        return

    DirectoryRename(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == "__main__":
    main()
