#!/usr/bin/env python3

name = input("Enter your name... ")
name = name.strip()

# Here your job will be to print 
# how many letters there 
# are in your name, and how many 
# of them are vowels: ['a'. 'e', 'i', 'o', 'u', 'y']

VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']

letters_count = len(name)
vowels_count = 0
for letter in name:
    if letter in VOWELS:
        vowels_count += 1

print("Your'r name {} has {} letters, of which {} vowels".format(name,
                                                                 letters_count,
                                                                 vowels_count))
