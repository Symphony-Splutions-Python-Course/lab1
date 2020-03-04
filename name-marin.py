name = input("Enter your name... ")
name_lower = name.lower()
# name = name.strip()
name_set = set(name_lower)
count =0
for x in name:
    if (x=='a' or x=='e' or x=='i'  or x=='o' or x=='u'):
        count+=1

print('Your name {} has {} letters,of which {} vowels'.format(name,len(name_set),count))