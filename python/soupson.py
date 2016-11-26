import sys
import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(requests.get('http://www.soupson.ca/?lang=en').text, "lxml")

menu = ""
for row in soup.find_all("div", class_="entry-content")[0].find_all("p")[1:]:
    menu += row.string + "\n"

if len(sys.argv) > 1:
    f1=open('./' + sys.argv[1], 'w+')
    f1.write(menuresult)
else:
    print menu
