a=6+4*9
print(a)
type(a)
print(type(a))

# dir(a)
# print(dir(a))

a=len("What's my name")
print(a)

#eksponenti
y=1**4 #eskponent mnozi prvoto cetiri pati megju sebe 1*1*1*1
print(y)
yy=2 ** 2 ** 6 # koga ima povekje eksponenti ide pravilo od desna strana,zatoa koristi parenting za da mozhe da presmeta ubavo
yy2=(2 ** 2) ** 6
print(yy)
print(yy2)
print(yy,yy2)


# dve // davaat floor na rezultatot
g=7//4
print(g)

g2=7/4
print(g2)


#mnozenje na string

tekst="banana"*3 # go dava kako eden cel string
tekst_myltiply=tekst*3

print(tekst_myltiply)
print(tekst)

## presmetka na radius na razlicni nacini cisto sintaksa vezbanje
# response = input("What is your radius? ")
# r = float(response)
# area = 3.14159 * r**2
# print("The area is ", area)

# print("The are is", 3.14159*int(float(input("what is your radius?"))**2))

# r = float( input("What is your radius? ") )
# print("The area is ", 3.14159 * r**2)

# % e ostatok
q= 7%3
print(q)

# prvo go deli 10 so 3 a potoa kako vtora vrednost pokazuva ostatok
e=divmod(10,3)
print(e)

##zadaca

data_render={}
zharko=["a","e","i","o","y","u"]

for x in range(2):
    new_key =("Name and Surname")
    new_name=input("enter your name and Surname")
    new_name=new_name.strip()
    print (len(new_name))
    data_render[new_key] = new_name
    tekst1 =str(new_name)
    print(tekst1)
   
   
    vowel_counts = {}
    for zharko in tekst1:
        count =tekst1.count(zharko)
        vowel_counts[zharko] = count
    print(vowel_counts)

print(data_render) 

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
    print(letter)
    if letter.isalpha():
        num_letters+=1
    else:
        letter = name[i+1].lower()
    if letter in ['a','e','i','o','u','y']:
            num_vowels+=1    

# print(letter)
print("Your name {} has {} letters, of which {} vowels".format(name, num_letters, num_vowels))