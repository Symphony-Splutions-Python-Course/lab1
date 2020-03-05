#!/usr/bin/env python3

import os
import sys


def main():
    # import ipdb; ipdb.set_trace()
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            text_stats = stats(filename)
            print(" {}  {} {} {}".format(*text_stats))
    else:
        content = sys.stdin.read()
        text_stats = content_stats(content)
        text_stats.append(len(content))
        text_stats.append(" - ")

        print(" {}  {} {} {}".format(*text_stats))
        

def content_stats(file_content):
    lines = file_content.splitlines()
    words = file_content.split()

    lines_count = len(lines)
    words_count = len(words)

    return [lines_count, words_count]

def stats(filename):
    """This function returns four values:
    - lines in the file,
    - words in the file,
    - size of the file,
    - file name
    """

    try:
        with open(filename, "r") as file:
            file_content = file.read()
            file_stats = content_stats(file_content)
            length = os.path.getsize(filename)
            file_stats.append(length)
            file_stats.append(file.name)

        return file_stats

    except FileNotFoundError as fnf_error:
        print("{}: {}".format(fnf_error.args[1], fnf_error.filename))
        # exit()
    except PermissionError as perm_error:
        print("{}: {}".format(perm_error.args[1], perm_error.filename))
        # exit()
    else:
        print("DONE")

if __name__ == "__main__":
    main()