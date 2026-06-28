import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://books.toscrape.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

data = []

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text

    data.append([title, price])

df = pd.DataFrame(data, columns=["Book Name", "Price"])

df.to_csv("books_dataset.csv", index=False)

print(df.head())
print("\nDataset Saved Successfully")