import requests
from bs4 import BeautifulSoup

URL = """https://www.worldometers.info/coronavirus/?fbclid=IwAR1OutjUurc_K4BH9F4smkLpC0yKfndoShfUtrs4cJZehqS7PQs0Ek85Xlw"""

# BAD_URL = "https://www.woarldometers.info/coronavirus/?fbclid=IwAR1OutjUurc_K4BH9F4smkLpC0yKfndoShfUtrs4cJZehqS7PQs0Ek85Xlw

response=requests.get(URL)
# response_dva = requests.get(BAD-URL)
status=response.status_code
body = response.text
content=response.content
type(content)
soup=BeautifulSoup(body,"html.parser")
numbers = soup.select("div.maincounter-number") 
all_ell=soup.find_all(class_="maincounter-number")
print(all_ell[0].text)


