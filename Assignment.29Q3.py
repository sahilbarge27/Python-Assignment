import sys
import shutil

source = sys.argv[1]

shutil.copy(source,"Demo.py")

print("File copied successfully into demo.py")

