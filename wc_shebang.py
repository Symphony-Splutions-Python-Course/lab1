#!usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

def main():
    #!/usr/bin/python3
import sys
import os
py_shebang = ""
bash_shebang = ""
files = sys.argv[1:]

def add_shebang(file_name, file_type):
    opened_file = open(file_name, "r+")
    content = opened_file.read()
    print(content)
    if content.split("\n")[0].__contains__("#!/"):
        pass
    else:
        opened_file.seek(0, 0)
        if file_type=="py":
            opened_file.write("#!/usr/bin/python3\n")
        if file_type in ["sh", "bash"]:
            opened_file.write("#!/bin/bash\n")
        opened_file.write(content)
    opened_file.close()


for file_name in files:
    extension = file_name.split(".")[1]
    if extension == "py":
        add_shebang(file_name, "py")
    elif extension in ["sh", "bash"]:
        add_shebang(file_name, "sh")
    else:
        pass

def preprend():
    try:
        with open(filename,"w+") as file:
            content = file.read()
            temp = content
            content.write("#!usr/bin/env python3")
            content.write(temp)
            return content
    except FileNotFoundError as fnf_error:
        error = "{}: {}\n".format(fnf_error.args[1], fnf_error.filename)
        sys.stderr.write(error)
    except PermissionError as perm_error:
        error = "{}: {}\n".format(perm_error.args[1], perm_error.filename)
        sys.stderr.write(error)
    except UnicodeDecodeError as error:
        error = "Binary File"
        sys.stderr.write(error)

if __name__ == "__main__":
    main()  