#!/usr/bin/python

from bs4 import BeautifulSoup
import requests
from datetime import date
import csv

filename = "covid19.txt"
file= open(filename,'w+')
URL = "https://www.worldometers.info/coronavirus/?fbclid=IwAR1OutjUurc_K4BH9F4smkLpC0yKfndoShfUtrs4cJZehqS7PQs0Ek85Xlw"

response = requests.get(URL)
text = response.text
soup = BeautifulSoup(text, 'html.parser')
stats =list()

for each_div in soup.findAll('div',{'class':'maincounter-number'}):
    stats.append(int(str(each_div.text).replace(",", "")))

ill=stats[0]
dead=stats[1]
percent = dead/ill * 100
perc = round(percent, 3)
x=date.today()
name=("Today is {}: Total Cases by now: {}, Deaths: {} Death to Cases Ratio:({}%)".format(x, ill, dead, perc))
#file.write(name)
#file.close()
opened_file=open("covid19.txt", "r+")
content = opened_file.read()
lines=opened_file.readlines()
with open('covid19.txt', 'r+') as file:
    if len(lines) == 0:
        file.write(name)
    elif content.split()[-1].__contains__(name):
        exit(1)
    else:
        opened_file.write(name)
        opened_file.write(content)
opened_file.close()




    


