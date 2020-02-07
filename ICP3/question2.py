import requests
from  bs4 import BeautifulSoup
import os

def examp():
    url="https://en.wikipedia.org/wiki/Deep_learning"
    source=requests.get(url)
    text=source.text
    soup=BeautifulSoup(text,"html.parser")
    print("the title is :",soup.title.string)
    reque_list=soup.find_all('a')
    for i in reque_list:
        print(i.get('href'))

examp()
