#!/usr/bin/env python3

import sys


def main():
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
<<<<<<< HEAD
            print(filename)
            #here we should go for every given filename.
        exit()

        filename = sys.argv[1]
        text_stats = stats(filename)
        print(" {}  {} {} {}".format(*text_stats))
    else:
        print("HERE COMES SYS INPUT!")
=======
            text_stats = stats(filename)
            if text_stats:
                print(" {}  {} {} {}".format(*text_stats))
    else:
        content = sys.stdin.read()
        text_stats = content_stats(content)
        text_stats.append(" - ")
        print(" {}  {} {} {}".format(*text_stats))


def content_stats(content):
    lines = content.splitlines()
    words = content.split()

    lines_count = len(lines)
    words_count = len(words)
    chars_count = len(content)

    return [lines_count, words_count, chars_count]

>>>>>>> bf9ef6059704272bbb0b2436de49b6a72fbe1651

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
            

            file_size = file.seek(0, 2)
            file_name = file.name

        return lines_count, words_count, file_size, file_name
    except FileNotFoundError as fnf_error:
<<<<<<< HEAD
        print(fnf_error)
=======
        error = "{}: {}\n".format(fnf_error.args[1], fnf_error.filename)
        sys.stderr.write(error)
        # exit(fnf_error.errno)
    except PermissionError as perm_error:
        error = "{}: {}\n".format(perm_error.args[1], perm_error.filename)
        sys.stderr.write(error)
        # exit(perm_error.errno)
>>>>>>> bf9ef6059704272bbb0b2436de49b6a72fbe1651

if __name__ == "__main__":
    main()