# Exercise 17 - Decode A Web Page 
# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.nytimes.com/'
# # url = 'http://github.com'
# r = requests.get(url)
# r_html = r.text

# soup = BeautifulSoup(r_html)
# title = soup.find('span', 'balancedHeadline').string

# print(title)

import requests
from bs4 import BeautifulSoup

# 1st way
# url = 'http://www.nytimes.com'
# r = requests.get(url)
# r_html = r.text
# soup = BeautifulSoup(r_html, "lxml")
# title = soup.findAll(class_="balancedHeadline")

# 2nd way
# r = requests.get("https://www.nytimes.com")
# soup = BeautifulSoup(r.content, "html.parser")
# titles = soup.find_all('span', {'class': 'balancedHeadline'})

# title.extend(soup.find_all("h1"))
# title.extend(soup.find_all("h2"))
# title.extend(soup.find_all("h3"))
# title.extend(soup.find_all("h4"))
# title.extend(soup.find_all("h5"))
# title.extend(soup.find_all("h6"))

# print([x.get_text() for x in title])

# for item in title:
#     try:
#         print item.text.strip()
#     except:
#         pass


# 3rd way
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, features="lxml")
 
for story_heading in soup.find_all(class_="balancedHeadline"): 
    if story_heading: 
        print(story_heading.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())