import csv
import requests
from bs4 import BeautifulSoup

get_request = requests.get("https://books.toscrape.com/index.html")
bs = BeautifulSoup(get_request.text, "html.parser")
all_product = bs.find_all("article", class_="product_pod")
books_list = []

for element in all_product:
    dictionary = {
        "title": element.find("h3").find("a")["title"],
        "price": element.find("p", class_="price_color").text,
        "available": element.find("p", class_="instock availability").text.strip()
    }
    books_list.append(dictionary)



with open("books.csv", mode="w", encoding="utf-8") as file:
   writer = csv.DictWriter(file, fieldnames=["title", "price", "available"])
   writer.writeheader()
   writer.writerows(books_list)