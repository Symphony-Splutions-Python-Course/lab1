#!/usr/bin/env python3
import sys

filename = sys.argv[1]
with open(filename,"r") as file:
    book = file.read()
    lines = book.splitlines()
    words = book.split()
    chars = 0

    for word in words:
        chars = chars + len(word)

    l = str(len(lines)).rjust(6)
    w = str(len(words)).rjust(6)
    c = str(chars).rjust(6)
    print(l, w, c, filename)