import logging

def CreateLog(logname):
    logging.basicConfig(
        filename=logname,
        level=logging.INFO,
        format="%(asctime)s : %(levelname)s : %(message)s"
    )
