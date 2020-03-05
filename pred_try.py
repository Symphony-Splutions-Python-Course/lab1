#!/usr/bin/env python3

import sys


def main():
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            print(filename)
            #here we should go for every given filename.
        exit()

        filename = sys.argv[1]
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
    try:
        with open(filename, "r") as file:
            file_content = file.read()
            lines = file_content.splitlines()
            words = file_content.split()

            lines_count = len(lines)
            words_count = len(words)
            text_stats = stats(filename)

            file_size = file.seek(0, 2)
            file_name = file.name

        return lines_count, words_count, file_size, file_name
    except FileNotFoundError as fnf_error:
        print(fnf_error)

if __name__ == "__main__":
    main()