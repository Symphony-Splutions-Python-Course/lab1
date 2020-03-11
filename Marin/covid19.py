#!/usr/bin/python


from bs4 import BeautifulSoup
import requests
from datetime import date
import csv
import fileinput

filename = "covid19.txt"
file = open(filename,'r+')

URL = "https://www.worldometers.info/coronavirus/?fbclid=IwAR1OutjUurc_K4BH9F4smkLpC0yKfndoShfUtrs4cJZehqS7PQs0Ek85Xlw"

response = requests.get(URL)
data = response.text
text = BeautifulSoup(data, 'html.parser')
today = date.today() 
stats = list()


for each_div in text.findAll('div',{'class':'maincounter-number'}):
    stats.append(int(str(each_div.text).replace(',','')))
dead = stats[1]
cases = stats[0]

percent = dead / cases * 100
percent = round(percent , 2)
firstl = file.readline().split(':')
today = date.strftime(today, "%Y-%m-%d")


if today == firstl[0]:
    file.seek(1,0)
    file.write(("{}: {}, {} ({}%)".format(today, cases, dead, percent)))
else:
    file.write(("{}: {}, {} ({}%)".format(today, cases, dead, percent)))


file.close()