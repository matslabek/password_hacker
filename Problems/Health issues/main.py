import requests

from bs4 import BeautifulSoup

website = input()

r = requests.get(website)

soup = BeautifulSoup(r.content, 'html.parser')

links = soup.find_all('a')

print([link.text for link in links if link.text and link.text[0] == 'S' and len(link.text) > 2
       and ('entity' in link['href'] or 'topics' in link['href'])])
