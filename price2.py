from urllib.request import urlopen
from bs4 import BeautifulSoup

url ="http://books.toscrape.com"

page = urlopen(url)
html = page.read().decode("utf-8")

print(html)