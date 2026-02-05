# DirectoryRename.py
import os
import sys
import logging

logging.basicConfig(filename="Rename.log", level=logging.INFO,
                    format="%(asctime)s : %(message)s")

def RenameFiles(dirname, ext1, ext2):
    try:
        if not os.path.isdir(dirname):
            print("Invalid Directory")
            return

        for file in os.listdir(dirname):
            if file.endswith(ext1):
                old = os.path.join(dirname, file)
                new = os.path.join(dirname, file.replace(ext1, ext2))
                os.rename(old, new)
                logging.info(file + " renamed")

        print("Renaming Done")

    except Exception as e:
        logging.exception(str(e))


def main():
    if len(sys.argv) != 4:
        print("Usage : DirectoryRename.py <Dir> <.txt> <.doc>")
        return

    RenameFiles(sys.argv[1], sys.argv[2], sys.argv[3])


if __name__ == "_main_":
    main()