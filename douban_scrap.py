from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime

today=datetime.date.today()
url = 'https://book.douban.com/chart?subcat=literary'
header = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35'}

ret = Request(url, headers=header)
html = urlopen(ret)
bs = BeautifulSoup(html, 'html.parser')

top10books = bs.find_all(name='a', attrs={'class':'fleft'})
authors = bs.find_all(name='p', attrs={'class':'subject-abstract color-gray'})
t = []
a = []

for i in top10books: t.append(i.text.strip())
for i in authors: a.append(i.text.strip())

books = {'书名': t,
         'info':a,
         'datetime':[today]*10}
books = pd.DataFrame(books)
books.to_csv('books.csv', encoding='utf-16')
