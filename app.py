from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys


def normalize_url(url):
    idx_search = url.find('B0') + 10
    return url[:idx_search]


def url_2_html(url):
    response = urlopen(url)
    html = response.read()
    html = str(html)
    return " ".join(html.split())


def get_ebook_price(kindle_price_in_html):
    index_price = kindle_price_in_html.find('$') + 2
    price = kindle_price_in_html[index_price:index_price+5]
    return price


def find_price_in_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    html_price_filter = soup.findAll(id="kindle-price")
    html_price_filter = str(html_price_filter)
    return get_ebook_price(html_price_filter)

# TODO Errors validations


# Main App
url = normalize_url(sys.argv[1])
html = url_2_html(url)
current_price = find_price_in_html(html)
print(current_price)
