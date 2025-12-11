import requests
from bs4 import BeautifulSoup
import time
import datetime

def check_new_balance(size="10.5", max_price=135):
    url = "https://www.newbalance.com/men/shoes/?prefn1=styleSubCategory&prefv1=Lifestyle"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    products = soup.find_all("li", class_="product-tile")

    print(">> Checking NewBalance.com...\n")
    for product in products:
        name_tag = product.find("a", class_="name-link")
        if not name_tag:
            continue
        name = name_tag.text.strip()
        if "9060" not in name:
            continue

        price_tag = product.find("span", class_="product-sales-price")
        if price_tag:
            price_text = price_tag.text.replace("$", "").strip()
            try:
                price = float(price_text)
            except:
                continue

            if price <= max_price:
                link = "https://www.newbalance.com" + name_tag["href"]
                print(f"> FOUND: {name} - ${price} - {link}")
    print(">> Done checking New Balance.\n")

# Run until your birthday
end_date = datetime.datetime(2025, 7, 7)

while datetime.datetime.now() < end_date:
    check_new_balance()
    print(">> Waiting 30 minutes before checking again...\n")
    time.sleep(1800)  # 1800 seconds = 30 minutes

print(">>
