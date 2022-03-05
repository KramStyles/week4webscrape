from requests import request
from bs4 import BeautifulSoup
from pprint import pprint

url = 'https://news.ycombinator.com/news'

req = request('GET', url)
soup = BeautifulSoup(req.text, 'html.parser')

# with open('soup.html', 'w') as my_soup:
#     my_soup.write(str(soup))

# anchors = soup.body.find_all('a')
# print(soup.title)
# print(soup.find('a')) # finds the first a tag
# print(soup.find(id='votelinks'))
# print(soup.select('.votelinks')) # allows us to find data using css selectors

# Let's get all the links that have over a 100 points in vote
titles = soup.body.select('.titlelink')
scores = soup.body.select('.score')

score_list = [int(score.getText().replace(' points', '')) for score in scores]
title_list = [{title.getText(): title.get('href', None)} for title in titles]

all = {}

for idx, value in enumerate(score_list):
    all[int(value)] = title_list[idx]

print(all)
pprint(all)