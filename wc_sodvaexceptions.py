#!/usr/bin/env python3

import sys


def main():
    #import ipdb; ipdb.set_trace()
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            text_stats = stats(filename)

            print(" {}  {} {} {}".format(*text_stats))
    else:
        print("HERE COMES SYS INPUT!")

def stats(filename):
    """This function returns four values:
    - lines in the file,
    - words in the file,
    - size of the file,
    - file name
    """
    # import ipdb; ipdb.set_trace()
    try:
        with open(filename, "r") as file:
            file_content = file.read()
            lines = file_content.splitlines()
            words = file_content.split()

            lines_count = len(lines)
            words_count = len(words)

            file_size = file.seek(0, 2)
            file_name = file.name

        return lines_count, words_count, file_size, file_name
    except FileNotFoundError as fnf_error:

        #import ipdb
        #impd.set_trace()
        print("{}: {}".format(fnf_error.args[1], fnf_error.filename))
        
    except PermissionError as perm_error:
        print("{}: {}".format(perm_error.args[1], perm_error.filename))
        exit()
        

if __name__ == "__main__":
    main()