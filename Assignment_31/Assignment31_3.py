import os
import sys
import shutil
from Logger import CreateLog
import logging

def DirectoryCopy(src, dest):
    if not os.path.isdir(src):
        logging.error("Source directory not found")
        return

    os.makedirs(dest, exist_ok=True)

    for file in os.listdir(src):
        shutil.copy(
            os.path.join(src, file),
            os.path.join(dest, file)
        )
        logging.info(f"Copied {file}")

def main():
    CreateLog("Copy.log")

    if len(sys.argv) != 3:
        logging.error("Invalid arguments")
        return

    DirectoryCopy(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
