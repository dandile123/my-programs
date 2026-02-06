import os
import sys
import hashlib
import logging
from logger import CreateLog

def CalculateChecksum(path):
    fd = open(path, 'rb')
    hobj = hashlib.md5()
    hobj.update(fd.read())
    fd.close()
    return hobj.hexdigest()

def DirectoryChecksum(dirname):
    if not os.path.isdir(dirname):
        logging.error("Invalid directory")
        return

    for file in os.listdir(dirname):
        path = os.path.join(dirname, file)
        if os.path.isfile(path):
            checksum = CalculateChecksum(path)
            logging.info(f"{file} : {checksum}")

def main():
    CreateLog("Checksum.log")

    if len(sys.argv) != 2:
        logging.error("Invalid arguments")
        return

    DirectoryChecksum(sys.argv[1])

if __name__ == "__main__":
    main()
