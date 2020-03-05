#!/usr/bin/env python3

import sys


def main():
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
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
        # exit(fnf_error.errno)
    except PermissionError as perm_error:
        error = "{}: {}\n".format(perm_error.args[1], perm_error.filename)
        sys.stderr.write(error)
        # exit(perm_error.errno)
    except UnicodeDecodeError as ud_error:
        ud_error = "Binary file\n"
        sys.stderr.write(ud_error)
        error = "Binary File"
        sys.stderr.write(error)


if __name__ == "__main__":
    main()
