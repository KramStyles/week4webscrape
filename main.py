from requests import request
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com/news'

req = request('GET', url)
soup = BeautifulSoup(req.text, 'html.parser')

# with open('soup.html', 'w') as my_soup:
#     my_soup.write(str(soup))

anchors = soup.body.find_all('a')
print(soup.title)
print(soup.find('a')) # finds the first a tag
print(soup.find(id='votelinks'))