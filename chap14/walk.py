#  Answer to exercise 14.1
#  Tenzin Choetso

import os

def walk(d_name):
    """Prints the names of all files in the given directory and its subdirectories.
    d_name: string name of a directory
    """
    for path, dirs, files in os.walk(d_name):
        for file in files:
            print os.path.join(path, file)


walk('.')
