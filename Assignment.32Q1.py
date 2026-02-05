import os
import hashlib
import logging

def DisplayChecksum(path):

    if not os.path.isdir(path):
        raise Exception("Directory does not exist")

    logging.basicConfig(filename="Log.txt",
                        level=logging.INFO,
                        format='%(asctime)s : %(message)s')

    logging.info("Scanning directory : " + path)

    for folder, subfolder, files in os.walk(path):
        for fname in files:

            fpath = os.path.join(folder, fname)

            checksum = hashfile(fpath)

            logging.info(f"{fname} : {checksum}")


def hashfile(path, blocksize=1024):

    afile = open(path, 'rb')
    hasher = hashlib.md5()

    buf = afile.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)

    afile.close()

    return hasher.hexdigest()