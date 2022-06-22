from urllib.request import urlopen
from bs4 import BeautifulSoup
from tqdm import tqdm
import requests


for i in tqdm(range(1,101)):
    page = "https://ssr1.scrape.center/detail/"+str(i)
    html = urlopen(page)
    bs = BeautifulSoup(html, 'html.parser')
    img = bs.find('img', {"class":"cover"})
    h2 = bs.find('h2')
    response = requests.get(img['src'])
    sep = '-'
    title = h2.text.split(sep, 1)[0]
    filename = "C:\\Users\\angel\\Pictures\\cover\\"+title+".png"
    file = open(filename,"wb")
    file.write(response.content)
    file.close()

print("Download complete!")