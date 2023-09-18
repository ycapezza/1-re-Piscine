import os
from pathlib import Path

def listdirs(rootdir):
    print(os.listdir(rootdir))
    for path in Path(rootdir).iterdir():
        if path.is_dir():
            print(path)
            listdirs(path)

cwd = os.getcwd()
#print(cwd)
listdirs(cwd)