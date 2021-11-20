import os
from urllib.request import urlopen
# from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
from dotenv import load_dotenv
# import sys

load_dotenv()

CAPA_DURA = os.getenv('CAPA_DURA')
CAPA_COMUM = os.getenv('CAPA_COMUM')
LIVRO_DE_BOLSO = os.getenv('LIVRO_DE_BOLSO')
KINDLE_UNLIMITED = os.getenv('KINDLE_UNLIMITED')
KINDLE_UNLIMITED_2 = os.getenv('KINDLE_UNLIMITED_2')
KINDLE = os.getenv('KINDLE')
PRODUTO_FISICO = os.getenv('PRODUTO_FISICO')
URL_ERROR = os.getenv('URL_ERROR')
print(KINDLE_UNLIMITED)


def url_to_html(url):
    response = urlopen(url)
    return response.read()


def get_book_price(html):
    # TODO PRODUTO/PREÇO NÃO ENCONTRADO

    content_html_page = BeautifulSoup(html, 'html.parser')
    selecao = content_html_page.find_all(
        'span', class_="a-size-base a-color-price a-color-price")

    return str(selecao)


def get_kindle_unlimited_price(html):
    content_html_page = BeautifulSoup(html, 'html.parser')
    selecao = content_html_page.find_all(
        'span', class_="extra-message olp-link")

    return str(selecao)


def get_product_price(html):
    content_html_page = BeautifulSoup(html, 'html.parser')
    selecao = content_html_page.find_all(
        'span', class_="a-price a-text-price a-size-medium apexPriceToPay")

    print(selecao)

    return str(selecao)


def get_formatted_price(price):
    price_start = price.find('$') + 1
    price_end = price.find(',') + 3
    price = price[price_start:price_end]
    price = price.replace('.', '')
    price = price.replace(',', '.')
    return float(price)


# Main App
html = url_to_html(PRODUTO_FISICO)
# html = url_to_html(sys.argv[1])
# price = get_book_price(html)
price = get_product_price(html)
# price = get_kindle_unlimited_price(html)
price = get_formatted_price(price)
print(price)
