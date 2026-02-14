import sys
import os
from logger_module import ConfigureLogger
from thread_monitor import DisplayThreadInfo
from file_monitor import DisplayOpenFilesInfo

def main():

    if len(sys.argv) != 2:
        print("Usage: python main.py <LogFileName>")
        exit()

    logfile = sys.argv[1]

    # Validation
    if not logfile.endswith(".log"):
        print("Please provide valid .log file")
        exit()

    ConfigureLogger(logfile)

    DisplayThreadInfo()
    DisplayOpenFilesInfo()
