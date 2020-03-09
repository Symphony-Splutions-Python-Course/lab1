#!/usr/bin/env python3

name = input("Enter your name... ")
name = name.strip()
# Here your job will be to print
# how many different letters there
# are in your name, and how many
# of them are vowels: ['a'. 'e', 'i', 'o', 'u',]


bukvi=''.join(sorted(set(name), key=name.index))
count=0
for i in range(len(bukvi)):
    letter=name[i]
    if letter in ['a','e','i','o','u','A','E','I','O','U']:
        count+=1

print("Your'r name {} has {} letters, of which {} vowels".format(name, len(bukvi), count))
