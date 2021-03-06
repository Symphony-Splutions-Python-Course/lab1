#!/usr/bin/env python3

import sys
import os  
# prvo sistemskite i se ostava 2 mesta megju import od razlicen tip


def main():
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            text_stats = stats(filename)
            try:
                print(" {}  {} {} {}".format(*text_stats))
            except:
                print("")

    else:
        content = sys.stdin.read()
        text_stats = content_stats(content)
        text_stats.append(" - ")
        try:
            print(" {}  {} {} {}".format(*text_stats))
        except:
            print("")


def content_stats(content):
    lines = content.splitlines()
    words = content.split()

    lines_count = len(lines)
    words_count = len(words)
    chars_count = len(content)

    return [lines_count, words_count, chars_count]


def stats(filename):
    """This function returns three values:
    - lines in the passed string,
    - words in the passed string,
    - size of the passed string,
    """

    try:
        with open(filename, "r") as file:
            content = file.read()
            stats = content_stats(content)
            stats.append(file.name)
        return stats
    except FileNotFoundError as fnf_error:
        error = "{}: {}\n".format(fnf_error.args[1], fnf_error.filename)
        sys.stderr.write(error)
        exit(fnf_error.errno)
    except PermissionError as perm_error:
        error = "{}: {}\n".format(perm_error.args[1], perm_error.filename)
        sys.stderr.write(error)
        exit(perm_error.errno)

if __name__ == "__main__":
    main()
