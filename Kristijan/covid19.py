import requests


URL = "https://www.worldometers.info/coronavirus/?fbclid=IwAR1OutjUurc_K4BH9F4smkLpC0yKfndoShfUtrs4cJZehqS7PQs0Ek85Xlw"

response = requests.get(URL)
text = response.text
soup = BeautifulSoup(text)

for each_div in soup.findAll('div',{'class':'maincounter-number'}):
    print (each_div.text)
    
