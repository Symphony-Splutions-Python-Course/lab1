#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
URL = "https://www.worldometers.info/coronavirus/?fbclid=IwAR1OutjUurc_K4BH9F4smkLpC0yKfndoShfUtrs4cJZehqS7PQs0Ek85Xlw"
content = requests.get(URL)
corona_stats=list()
soup = BeautifulSoup(content.text, 'html.parser')

for el in soup.find_all(class_ = "maincounter-number"):
    corona_stats.append(int(str(el.text).replace(",", "")))

dd_ratio = corona_stats[1]/corona_stats[0]
print("death to disease ratio: ", dd_ratio*100, "%")
dr_ratio = corona_stats[2]/corona_stats[0]
print("disease to recovery ratio", dr_ratio*100, "%")
