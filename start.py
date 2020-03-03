n=10
for i in range (n):
    print(i)



#test za 2ra verzija za push na github

n=20
for i in range (n):
    print(i)

usefull_strip="123456\n7"
print(usefull_strip)

print(usefull_strip.rstrip())


# da dodadesh nesto pomegju indeksi
list=["asdda","asdxcc"]
x=",".join(list) #ili mozhes x="\n".join(list)
print(x)

#ke dade tekst koj pomesten na desno so vkupna golemina na tekst space atributot
y="asdj".rjust(20)
print(y)


#da se vidi do kolku se povtoruva den zbor
razno="""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
print(razno)
zborovi = razno.split() # se splituva sekoj zbor kako posebno i se pravi string na sekoe prazno mesto
print(zborovi)
zborovi2=razno.split(".") #se splituva kako string do sekoja tocka
print(zborovi2)

niza={}
for item in zborovi:
    if item in niza.keys(): #da ne te buni ova .keys bidejki taka se dodava a ne e da prebaruva po keys
        niza[item]=niza[item]+1
    else:
        niza[item]=1

print(niza)




# #zadaca

# from datetime import date
# datetime.today(1990,9,15)
# today=date.today()
# day=today.day()

# days=["Sunday","Monday","Tuesday","Wednesday", "Thirsday","Friday","Saturday"]

x=3

while x<10:
    print(x)
    x+=1

#printanje elka

row="*"

for i in range(9):
    print(row.center(19))
    row=row+"**"



