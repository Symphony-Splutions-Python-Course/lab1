from datetime import date
import requests

from bs4 import BeautifulSoup
import csv

CSV_FILE = ("stats.csv")
CSV_HEADERS = "Date,Total Cases,New Cases,Total Deaths,New Deaths,Total Recovered,Active Cases,Serious(Critical),Tot Cases/1M pop"

URL = "https://www.worldometers.info/coronavirus/"
today = date.strftime(date.today(),"%Y-%m-%d")#vakov format radi sort

csv_file_r = open(CSV_FILE,"r")
csv_file_w = open(CSV_FILE,"w")

csv_reader = csv.reader(csv_file_r)
csv_writer = csv.writer(csv_file_w)

response = requests.get(URL)
text = response.text
soup = BeautifulSoup(text, "html.parser")


table_rows = soup.find_all("tr")#site rows
last_row = table_rows[-1].text.split()[1:]


total_values = [value.replace(",","") for value in last_row]
total_values.insert(0,today)
print(csv_reader)
total = ", ".join(total_values)
first_line = csv_reader.readline().split()
print(first_line)

if today == first_line[0]:
    csv_writer.writerow(total)
else:
    csv_writer.writerow(total)

