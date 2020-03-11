
from datetime import date
import requests

import bs4

CSV_FILE = "stats.txt"
CSV_HEADER = "Date,Total Cases,New Cases,Total Deaths,New Deaths,Total Recovered,Active Cases,Serious (Critical),Tot Cases/1M pop"

URL = "https://www.worldometers.info/coronavirus/?fbclid=IwAR1OutjUurc_K4BH9F4smkLpC0yKfndoShfUtrs4cJZehqS7PQs0Ek85Xlw"


today = date.strftime(date.today(), 
                          "%Y-%m-%d")


response = requests.get(URL)
text = response.text
soup = bs4.BeautifulSoup(text, "html.parser")                                             
table_rows = soup.find_all("tr")
totals_row = table_rows[-1].text.split()[1:]
totals_values = [value.replace(",","") for value in totals_row]
totals_values.insert(0, today)
totals = ", ".join(totals_values)

print(totals)