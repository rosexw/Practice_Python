# 19-decode-webpage2.py

import requests
from bs4 import BeautifulSoup


source = requests.get("http://content.time.com/time/magazine/article/0,9171,2005869,00.html").text
soup = BeautifulSoup(source, 'lxml')

print(soup.title.text)



for i in soup.find_all('p'):
    article = i.text
    print(article)
