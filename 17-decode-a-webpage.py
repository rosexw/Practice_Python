# Exercise 17 - Decode A Web Page 
# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
nyt_html = r.text

soup = BeautifulSoup(nyt_html,features="html.parser")
for h2 in soup.findAll("h2", class_="css-bzeb53 esl82me2"):
    print(h2.text)