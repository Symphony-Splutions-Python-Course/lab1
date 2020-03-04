#!/usr/bin/env python3

name = input("Enter your name... ")
name = name.strip()

# Here your job will be to print 
# how many letters there 
# are in your name, and how many 
# of them are vowels: ['a'. 'e', 'i', 'o', 'u', 'y']
num_vowels = 0
num_letters = 0
for i in range(len(name)):
    letter = name[i].lower()
    if letter.isalpha():
        num_letters+=1
        if letter in ['a','e','i','o','u']:
            num_vowels+=1    


print("Your name {} has {} letters, of which {} vowels".format(name, num_letters, num_vowels))

