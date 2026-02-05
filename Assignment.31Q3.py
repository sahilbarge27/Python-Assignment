# DirectoryCopy.py
import os
import sys
import shutil
import logging

logging.basicConfig(filename="Copy.log", level=logging.INFO)

def CopyDir(src, dest):
    try:
        if not os.path.isdir(src):
            print("Source not present")
            return

        if not os.path.exists(dest):
            os.mkdir(dest)

        for file in os.listdir(src):
            shutil.copy(os.path.join(src, file), dest)

        logging.info("Files copied")
        print("Copy Successful")

    except Exception as e:
        logging.exception(str(e))


def main():
    if len(sys.argv) != 3:
        print("Usage : DirectoryCopy.py Demo Temp")
        return

    CopyDir(sys.argv[1], sys.argv[2])


if __name__ == "_main_":
    main()