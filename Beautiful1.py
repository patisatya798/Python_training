from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"

page = urlopen(url)
html = page.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")

print(soup.find("title").text)
print(soup.find_all("img"))

image1 , image2 = soup.find_all("img")

print(image1["src"])

print(soup.find_all("img" , src="/static/dionysus.jpg"))