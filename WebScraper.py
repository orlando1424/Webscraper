from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as beautifulSoup

# https://www.youtube.com/watch?v=XQgXKtPSzUI  youtube video for reference of script

my_url = 'https://www.newegg.com/Product/ProductList.aspx?Submit=StoreIM&Depa=1&Category=38'

# Opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# HTML Parser
page_soup = beautifulSoup(page_html, "html.parser")

# Grabs each product
containers = page_soup.findAll("div", {"class": "item-container"})


filename = "products.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping \n"
f.write(headers)

for container in containers:

    divWithInfo = containers[0].find("div", "item-info")

    brand = divWithInfo.div.img["title"]

    title_container = container.findAll("a", {"class": "item-title"})
    product_name = title_container[0].text
    shipping_container = container.findAll("li", {"class": "price-ship"})
    shipping = shipping_container[0].text.strip()

    print("brand: " + brand)
    print("product name: " + product_name)
    print("shipping: " + shipping)

    f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")
f.close()