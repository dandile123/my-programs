import os
import sys
import shutil
from logger import CreateLog
import logging

def DirectoryCopyExt(src, dest, ext):
    if not os.path.isdir(src):
        logging.error("Source directory not found")
        return

    os.makedirs(dest, exist_ok=True)

    for file in os.listdir(src):
        if file.endswith(ext):
            shutil.copy(
                os.path.join(src, file),
                os.path.join(dest, file)
            )
            logging.info(f"Copied {file}")

def main():
    CreateLog("CopyExt.log")

    if len(sys.argv) != 4:
        logging.error("Invalid arguments")
        return

    DirectoryCopyExt(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == "__main__":
    main()
