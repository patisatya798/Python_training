import requests
from bs4 import BeautifulSoup
import csv
import re

def scrape_books_to_csv(url, filename):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    products = soup.select(".product_pod")

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["S.No", "Name", "Price", "Quantity", "Total"])

        grand_total = 0
        maximum = 0 

        for i, product in enumerate(products, start=1):
            name_tag = product.find("h3").find("a")
            name = name_tag["title"] if name_tag else "Unknown"

            price_tag = product.find("p", class_="price_color")

            if price_tag:
                raw_price = price_tag.text.strip()
                numbers = re.findall(r"\d+", raw_price)
                price = int(numbers[0]) if numbers else 0
            else:
                price = 0

            quantity = i + 1
            total = price * quantity
            grand_total += total

            if price > maximum:
                maximum = price

            writer.writerow([i, name, price, quantity, total])

    print("CSV created!")
    print("Max Price:", maximum)
    print("Grand Total:", grand_total)


scrape_books_to_csv("https://books.toscrape.com/", "products.csv")