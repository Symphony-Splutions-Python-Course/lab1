import sys
import os
files = sys.argv[1:]

def add_shebang(file_name, file_type):
    opened_file = open(file_name, "a+")
    content = opened_file.read()
    if content.__contains__("#!/"):
        pass
    else:
        opened_file.seek(0)
        if file_type=="py":
            opened_file.write("#!/usr/bin/python3\n" + content)
        if file_type in ["sh", "bash"]:
            opened_file.write("#!/bin/bash\n" + content)
    opened_file.close()


for file_name in files:
    extension = file_name.split(".")[1]
    if extension == "py":
        add_shebang(file_name, "py")
    elif extension in ["sh", "bash"]:
        add_shebang(file_name, "sh")
    else:
        pass
