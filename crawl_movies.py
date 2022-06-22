# 爬取影视网站上第一页的信息
from urllib.request import urlopen
from bs4 import BeautifulSoup
import xlwt
import pandas as pd

html = urlopen("https://ssr1.scrape.center/")
bs = BeautifulSoup(html, 'html.parser')
titles = bs.find_all('h2')
span = bs.find_all('span')
movies = {}
attributes = []
for movie in titles:
    movies[movie.text] = []
i = 0
for s in span:
    if(i<10):
        if(len(s.text)>1 and s.text!="Scrape" and s.text!= " / "):
            attributes.append(s.text)
        if(list(movies)[i]=="楚门的世界 - The Truman Show"):
            if(len(s.text)>3):
                movies[list(movies)[i]] = attributes
                attributes = []
                i+=1
        elif(len(s.text)>10 ):
            movies[list(movies)[i]] = attributes
            attributes = []
            i+=1
print(movies)
