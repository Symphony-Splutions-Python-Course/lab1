
#!/usr/bin/env python3
import sys
import os
for i in range(1, len(sys.argv)):
    filename = sys.argv[i]
    with open(filename, "r") as file:
        book = file.read()

        lines = book.splitlines()
        words = book.split()
        chars = os.path.getsize(filename)
        print(len(lines), len(words), chars, filename)
    file.close()
    try:
        file = open(filename, "r")
    except IOError:
        print("Error opening the file")

    try:
        with open(filename,"r") as file:
            book = file.read()
    except:
        print("Error reading the file")

