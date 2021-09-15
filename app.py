from urllib.request import urlopen
from bs4 import BeautifulSoup
# import sys


def url_to_html(url):
    response = urlopen(url)
    return response.read()


def find_price_in_html(html):
    content_html_page = BeautifulSoup(html, 'html.parser')
    # price # id tag for physical books
    # kindle-price # id tag for eBooks
    # price_inside_buybox # id tag for physical products

    return content_html_page.find(id="price").get_text()


def get_formatted_price(price):
    price_index = price.find('$') + 2
    price = price[price_index:len(price)+1]
    price = price.replace('.', '')
    price = price.replace(',', '.')
    return float(price)


# url = 'https://www.amazon.com.br/1984-Exclusiva-Amazon-George-Orwell/dp/6586490162/ref=tmm_hrd_swatch_0?_encoding=UTF8&qid=1631567074&sr=1-3'

url = 'https://www.amazon.com.br/Hit-Makers-Things-Become-Popular/dp/0241216028/ref=tmm_hrd_swatch_0?_encoding=UTF8&qid=&sr='

# Main App
html = url_to_html(url)
# html = url_to_html(sys.argv[1])
price = find_price_in_html(html)
price = get_formatted_price(price)
print(price)
