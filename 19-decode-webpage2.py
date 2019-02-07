# 19-decode-webpage2.py

import requests
from bs4 import BeautifulSoup

source = requests.get("http://content.time.com/time/magazine/article/0,9171,2005869,00.html").text
source2 = requests.get("http://content.time.com/time/magazine/article/0,9171,2005869-2,00.html").text
soup = BeautifulSoup(source, 'lxml')
soup2 = BeautifulSoup(source2, 'lxml')

print(soup.title.text)

for i in soup.find_all('p'):
    article = i.text
    print(article)

for j in soup2.find_all('p'):
    article2 = j.text
    print(article2)