import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=Sri+Lanka'
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')

#Just all the anchors
# anchors = soup('a')
# for an in anchors:
#    print(an.get('href'))

#Just all the headings    
headings = soup('h3')
for heading in headings:
    print(heading.find('div').text)
    #print(heading.parent)
    print(heading.parent.get('href'))
    print("\n")
    
#This only retrieve the results from the first page of search results.
#Can you get the results from the second page as well? What is the GET parameter you need to include to get the rest of the search results?