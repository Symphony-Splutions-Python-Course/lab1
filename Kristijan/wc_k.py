#!/usr/bin/env python3

import sys #da postojat paketite vo namespace()
import os  #=/=


def main(): #definirame funkcija (davas vlezni, ocekuvas izlezni rezutlati)
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            if not os.path.isfile(filename):
                continue
            text_stats = stats(filename)
            if text_stats:
                print(" {}  {} {} {}".format(*text_stats))
    else:
        content = sys.stdin.read()
        text_stats = content_stats(content)
        text_stats.append(" - ")
        print(" {}  {} {} {}".format(*text_stats))


def content_stats(content): #zema argument content broi
    if type(content) != 'str':
        print("Content is not a string")
        exit(1)
    lines = content.splitlines() #deli na redovi
    words = content.split() #deli na zborovi

    lines_count = len(lines) #broi redovi
    words_count = len(words) #broi zborovi
    chars_count = len(content) #broi karakteri

    return [lines_count, words_count, chars_count]


def stats(filename): #zema filename
    """This function returns three values:
    - lines in the passed string,
    - words in the passed string,
    - size of the passed string,
    """ #komentar

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
    except UnicodeDecodeError as error:
        error = "Binary File"
        sys.stderr.write(error)


if __name__ == "__main__":
    main()
