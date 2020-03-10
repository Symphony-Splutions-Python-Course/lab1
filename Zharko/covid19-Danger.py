import requests
from bs4 import BeautifulSoup
import datetime

URL = """https://www.worldometers.info/coronavirus/?fbclid=IwAR1OutjUurc_K4BH9F4smkLpC0yKfndoShfUtrs4cJZehqS7PQs0Ek85Xlw"""

# BAD_URL = "https://www.woarldometers.info/coronavirus/?fbclid=IwAR1OutjUurc_K4BH9F4smkLpC0yKfndoShfUtrs4cJZehqS7PQs0Ek85Xlw

response=requests.get(URL)
# response_dva = requests.get(BAD-URL)
status=response.status_code
body = response.text
content=response.content
print(content)
print(body)
type(content)
soup=BeautifulSoup(body,"html.parser")
# numbers = soup.select("div.maincounter-number")
# print(numbers) ova e isto so all_ell 
all_ell=soup.find_all(class_="maincounter-number")
print(all_ell[0].text)


statistike =list()

for el in all_ell:
    statistike.append(int(str(el.text).replace(",","")))

print(statistike)

for i in all_ell:
    x=datetime.datetime.now()
    print(i.text,x)

dd_ratio = statistike[1]/statistike[0]
print("death to disease ratio: ", dd_ratio*100, "%")
dr_ratio = statistike[1]/statistike[0]
print("disease to recovery ratio", dr_ratio*100, "%")

y=datetime.datetime.now()
print("Vreme :{} Zarazeni : {}, Mrtvi : {}, Soodnos : {}%)".format(y, statistike[0],statistike[1],dd_ratio*100))