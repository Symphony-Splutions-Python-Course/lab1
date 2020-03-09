#!usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

def main():
    if len(sys.argv)>1:
        for filename in sys.argv[1:]:
            print("zdr")
            if not os.path.isfile(filename):
                print(filename, "is not a file")
                continue
    else:
        content = sys.stdin.read()
        text = adding(content)
        print(text)


def adding():
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