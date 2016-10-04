import sys
import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(requests.get('http://www.soupson.ca/?lang=en').text, "lxml") 

result = ""
for row in soup.find_all("div", class_="entry-content")[0].find_all("p")[1:]:
    result = result + row.string + "\n"

if len(sys.argv) > 1:
    f1=open('./menu', 'w+')
    f1.write(result)
else:
    print result
