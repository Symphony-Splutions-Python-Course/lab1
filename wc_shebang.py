#!bin/usr/env python3

import sys
import os
import re

files = sys.argv[1:]

def prepend_shebang(filename):
    with open(filename, "r+") as file:
        content = file.read()
        print(file.readline())
        if re.search('#!',content.readline()) == True :
            pass    
        else:
            extension = os.path.splitext(file)[1]
            if extension == '.py':
                filename.write("#!usr/bin/env python3\n")
            if extension == '.sh' or extension == '.bash':
                filename.write("#!/bin/bash\n")

for filename in files:
    prepend_shebang(filename)