# DirectoryCopyExt.py
import os
import sys
import shutil
import logging

logging.basicConfig(filename="CopyExt.log", level=logging.INFO)

def CopyExt(src, dest, ext):
    try:
        if not os.path.isdir(src):
            print("Invalid source")
            return

        if not os.path.exists(dest):
            os.mkdir(dest)

        for file in os.listdir(src):
            if file.endswith(ext):
                shutil.copy(os.path.join(src, file), dest)

        logging.info("Extension files copied")
        print("Copy Successful")

    except Exception as e:
        logging.exception(str(e))


def main():
    if len(sys.argv) != 4:
        print("Usage : DirectoryCopyExt.py Demo Temp .exe")
        return

    CopyExt(sys.argv[1], sys.argv[2], sys.argv[3])


if __name__ == "_main_":
    main()