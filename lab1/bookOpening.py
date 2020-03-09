
#! /usr/bin/env python3
import sys
print(sys)

filename = sys.argv[1]
print(filename)
with open(filename,"r") as file:
    book = file.read()
    lines=book.splitlines()
    words=book.split()
    n=0

    for i in words:
        n+=len(i)

    l=str(len(lines)).rjust(10)
    w=str(len(words)).rjust(10)
    c=str(n).rjust(10)
    print (l,w,c,filename)