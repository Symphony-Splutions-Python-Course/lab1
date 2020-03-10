import requests
from bs4 import BeautifulSoup

URL = "https://www.worldometers.info/coronavirus/?fbclid=IwAR1OutjUurc_K4BH9F4smkLpC0yKfndoShfUtrs4cJZehqS7PQs0Ek85Xlw"

response = requests.get(URL)
print(response.status_code)

data = response.text
text = BeautifulSoup(data, "html.parser") #data mi e body a text mi e soup

for each_div in text.findAll('div',{'class':'maincounter-number'}):
    print (each_div.text)

