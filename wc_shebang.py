#!bin/usr/env python3

import sys
import os

files = sys.argv[1:]

def prepend_shebang(filename):
    with open(filename, "r+") as file:
        content = file.read()
        if content.readline().__contains__ == "#!":
            pass
        else:
            if os.path.splitext('.py')
                filename.write("#!usr/bin/env python3\n")
            if os.path.splitext('.bash') || os.path.splitext('.sh')
                filename.write("#!/bin/bash\n")




for filename in files:
    prepend_shebang(filename)