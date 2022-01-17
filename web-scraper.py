import requests
from bs4 import BeautifulSoup
import time


# -------------------------------------------------------------------------

print('Made By Sir Distru')
tx = "Developing The Future..."
for char in list("".join(tx.strip())):
    time.sleep(0.5)
    print(char)
# --------------------------------------------------------------------------

print('Time to start scraping the Web!')
link = 'https://www.ebay.it/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw='
search = str(input('Now input the item that you want to search: '))
furl = link + search
g = requests.get(furl)
html = BeautifulSoup(g.text, features="html.parser")
#res = html.find("span", attrs={"data-index":"1"})
#print(str(res))

title = html.findAll("title")
Nome = html.findAll(class_="s-item__title")
prezzo = html.find(class_="s-item__price")
nome1 = html.findAll('h3', class_="s-item__title")
print(nome1)
print(title)
print(Nome)
print(prezzo)

link2 = 'https://www.newegg.com/p/pl?d='
search2 = input('Elemento da cercare su NewEgg: ')
url2 = link2 + search2
g2 = requests.get(url2)
html2 = BeautifulSoup(g2.text, features="html.parser")
Nome2 = html2.findAll(class_="item-title")
print(Nome2)

#NOT COMPLETED, DO NOT REPOST WITHOUT CONSENS
