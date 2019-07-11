
from bs4 import BeautifulSoup as bs
from googlesearch import search_news
import requests
import re



def getText(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
    }
    r = requests.get(url, headers=headers)

    print(r)

    soup = bs(r.text, 'html.parser')

    for paragraph in soup.find_all('p'):
        if paragraph.find(['img', 'time', 'span', 'style', 'aside']):
            continue
        for tag in ['a', 'br']:
            for match in paragraph.find_all(tag):
                match.replaceWithChildren()
    ##    for tag in paragraph(['None']):
    ##        tag.decompose()

##        if paragraph.get('class'):
##            continue
        print(paragraph.getText())



##urls = search_news('jamie dimon', stop=1)
##
##for url in urls:
##    print(url)
##    getText(url)


##url = 'https://www.pcgamer.com/amd-radeon-rx-5700-and-rx-5700-xt-review-in-progress/'
##url = 'https://www.bloomberg.com/news/articles/2018-11-20/jamie-dimon-vindicated-bitcoin-s-back-to-where-he-cried-fraud'
##url = 'https://gizmodo.com/a-last-minute-price-drop-makes-amds-new-graphics-cards-1836074271'
url = 'https://www.barrons.com/articles/jpmorgan-chase-ceo-jamie-dimon-interview-51559945813'

getText(url)








