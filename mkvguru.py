import time
import requests
from bs4 import BeautifulSoup


url = "https://mkvguru.in/avatar-the-way-of-water/"

def mkv(url):
    client = requests.session()
    r = client.get(url)
    soup = BeautifulSoup (r.text, "html.parser")
    gdtot = soup.select('a[href*="gdtot"]')
    file = soup.select('a[href*="filepress"]')
    for a in gdtot:
         link = a["href"]
         print(link) 
    for a in file:
         link = a["href"]
         print(link)
print(mkv(url))
