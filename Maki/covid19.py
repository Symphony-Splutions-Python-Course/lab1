#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
import datetime
URL = "https://www.worldometers.info/coronavirus/?fbclid=IwAR1OutjUurc_K4BH9F4smkLpC0yKfndoShfUtrs4cJZehqS7PQs0Ek85Xlw"
content = requests.get(URL)

file_name = "covid19_" + str(datetime.datetime.today()).split()[0] + ".txt"
f = open(file_name, "w+")
f.write("Coronavirus statistics exactly on: " + str(datetime.datetime.today()) + "\n\n")
corona_stats = list()
soup = BeautifulSoup(content.text, 'html.parser')

for el in soup.find_all(class_ = "maincounter-number"):
    corona_stats.append(int(str(el.text).replace(",", "")))

dd_ratio = corona_stats[1]/(corona_stats[0]+ corona_stats[1])
dd_ratio_str = "death to disease ratio: " + str(round(dd_ratio*100,2)) + "%"
print(dd_ratio_str)
f.write(dd_ratio_str + "\n")

dr_ratio = corona_stats[2]/(corona_stats[0]+corona_stats[2])
dr_ratio_str = "disease to recovery ratio: " + str(round(dr_ratio*100,2)) + "%"
print(dr_ratio_str)
f.write(dr_ratio_str + "\n")

currently_sick = corona_stats[0]
print("diseased at the moment: ", currently_sick)
f.write("diseased at the moment: " + str(currently_sick) + "\n")

total_cases = corona_stats[0]+corona_stats[1]+corona_stats[2]
print("total recorded cases: ", total_cases)
f.write("total recorded cases: " + str(total_cases) + "\n")

f.seek(0,0)
print("=================")
print(f.read())
f.close()
