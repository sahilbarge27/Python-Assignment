import os
import hashlib
import logging

def RemoveDuplicate(path):

    if not os.path.isdir(path):
        raise Exception("Directory not exist")

    logging.basicConfig(filename="Log.txt",
                        level=logging.INFO,
                        format='%(asctime)s : %(message)s')

    checksums = {}

    for folder, subfolder, files in os.walk(path):

        for fname in files:

            fpath = os.path.join(folder, fname)

            file_hash = hashfile(fpath)

            if file_hash in checksums:

                os.remove(fpath)

                logging.info("Deleted : " + fpath)

            else:
                checksums[file_hash] = fpath


def hashfile(path, blocksize=1024):

    afile = open(path, 'rb')
    hasher = hashlib.md5()

    buf = afile.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)

    afile.close()

    return hasher.hexdigest()