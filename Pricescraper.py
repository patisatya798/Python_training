from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://web-scraping.dev/products"

page = urlopen(url)
html = page.read().decode("utf-8")
print(html)

# soup = BeautifulSoup(html, "html.parser")

# products = soup.select(".product")

# for product in products:
#     name = product.select_one("h3")
#     price = product.select_one(".price")

#     if name and price:
#         print(name.text.strip(), price.text.strip())