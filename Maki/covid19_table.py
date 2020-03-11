from bs4 import BeautifulSoup
import requests
from datetime import datetime

URL = "https://www.worldometers.info/coronavirus/?fbclid=IwAR1OutjUurc_K4BH9F4smkLpC0yKfndoShfUtrs4cJZehqS7PQs0Ek85Xlw"
content = requests.get(URL)
soup = BeautifulSoup(content.text, "html.parser")
table_stats = str(soup.findAll('tr')[-1].text).replace(",", "").split()[1:]
str_stats = "{} {} {} {} {} {} {} {}".format(*table_stats)
print(str_stats)