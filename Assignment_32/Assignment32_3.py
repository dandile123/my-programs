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

def RemoveDuplicate(dirname):
    if not os.path.isdir(dirname):
        logging.error("Invalid directory")
        return

    checksum_map = {}

    for file in os.listdir(dirname):
        path = os.path.join(dirname, file)
        if os.path.isfile(path):
            checksum = CalculateChecksum(path)
            if checksum in checksum_map:
                os.remove(path)
                logging.info(f"Deleted duplicate : {file}")
            else:
                checksum_map[checksum] = file

def main():
    CreateLog("Log.txt")

    if len(sys.argv) != 2:
        logging.error("Invalid arguments")
        return

    RemoveDuplicate(sys.argv[1])

if __name__ == "__main__":
    main()
