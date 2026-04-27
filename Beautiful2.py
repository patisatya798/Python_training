from bs4 import BeautifulSoup
from urllib.request import urlopen

base_url = "http://olympus.realpython.org/profiles"
url = "http://olympus.realpython.org/profiles"

page = urlopen(url)

html = page.read().decode("utf-8")

soup = BeautifulSoup(html , "html.parser")

for link in soup.find_all("a"):
    full_url = base_url + link["href"]
    print(full_url)
