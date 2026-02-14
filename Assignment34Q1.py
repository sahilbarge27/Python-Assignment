import os
import zipfile
import datetime

# Create Logs folder
def CreateLogFolder():
    if not os.path.exists("Logs"):
        os.mkdir("Logs")

# Write log
def WriteLog(message):
    CreateLogFolder()
    filename = "Logs/BackupLog.txt"
    with open(filename, "a") as f:
        f.write(message + "\n")

# Backup function
def BackupDirectory(source, exclude_ext):
    try:
        if not os.path.exists(source):
            WriteLog("ERROR: Source directory does not exist")
            return None

        start_time = datetime.datetime.now()
        WriteLog(f"Backup Started at: {start_time}")

        zipname = f"Backup_{start_time.strftime('%Y%m%d_%H%M%S')}.zip"
        files_copied = 0

        with zipfile.ZipFile(zipname, 'w') as zipf:
            for foldername, subfolders, filenames in os.walk(source):
                for file in filenames:
                    if not file.endswith(tuple(exclude_ext)):
                        filepath = os.path.join(foldername, file)
                        zipf.write(filepath)
                        files_copied += 1

        WriteLog(f"Files Copied: {files_copied}")
        WriteLog(f"Zip File Created: {zipname}")
        WriteLog("Backup Completed Successfully\n")

        return zipname, files_copied

    except Exception as e:
        WriteLog(f"ERROR: {str(e)}")
        return None

# Restore function
def RestoreBackup(zipname, destination):
    try:
        if not os.path.exists(zipname):
            WriteLog("ERROR: Zip file not found")
            return

        with zipfile.ZipFile(zipname, 'r') as zipf:
            zipf.extractall(destination)

        WriteLog(f"Backup Restored to {destination}\n")

    except Exception as e:
        WriteLog(f"ERROR: {str(e)}")

# Maintain History
def UpdateHistory(date, files, size):
    with open("History.txt", "a") as f:
        f.write(f"{date} | Files: {files} | Size: {size} bytes\n")

def ShowHistory():
    if os.path.exists("History.txt"):
        with open("History.txt", "r") as f:
            print(f.read())
    else:
        print("No History Found")