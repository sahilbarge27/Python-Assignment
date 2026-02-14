import sys
import os
import datetime
from MarvellousBackup import *

def main():

    # Restore Feature
    if len(sys.argv) == 4 and sys.argv[1] == "--restore":
        zipfile_name = sys.argv[2]
        destination = sys.argv[3]
        RestoreBackup(zipfile_name, destination)
        return

    # History Feature
    if len(sys.argv) == 2 and sys.argv[1] == "--history":
        ShowHistory()
        return

    # Normal Backup
    if len(sys.argv) < 2:
        print("Usage:")
        print("python Script.py DirectoryPath")
        print("python Script.py --restore ZipFile Destination")
        print("python Script.py --history")
        return

    source = sys.argv[1]

    # Exclude extensions
    exclude_ext = ['.tmp', '.log', '.exe']

    result = BackupDirectory(source, exclude_ext)

    if result is not None:
        zipname, files = result
        size = os.path.getsize(zipname)
        date = datetime.datetime.now()
        UpdateHistory(date, files, size)


if _name_ == "_main_":
    main()