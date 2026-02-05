# DirectoryFileSearch.py
import os
import sys
import logging

logging.basicConfig(filename="FileSearch.log", level=logging.INFO,
                    format="%(asctime)s : %(message)s")

def DisplayFiles(dirname, extension):
    try:
        if not os.path.isdir(dirname):
            print("Invalid Directory")
            return

        logging.info("Searching files with extension " + extension)

        for file in os.listdir(dirname):
            if file.endswith(extension):
                print(file)

    except Exception as e:
        logging.exception("Error : " + str(e))


def main():
    if len(sys.argv) != 3:
        print("Usage : DirectoryFileSearch.py <Directory> <Extension>")
        return

    DisplayFiles(sys.argv[1], sys.argv[2])


if __name__ == "_main_":
    main()