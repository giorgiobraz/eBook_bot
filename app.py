import os
from urllib.request import urlopen
# from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
from dotenv import load_dotenv
# import sys
load_dotenv()


# TODO Send Push Notification

KINDLE = os.getenv('KINDLE')


def url_to_html(url):
    response = urlopen(url)
    return response.read()


def parse_price(price):
    price_start = price.find('$') + 1
    price_end = price.find(',') + 3
    price = price[price_start:price_end]
    price = price.replace('.', '')
    price = price.replace(',', '.')
    return float(price)


def get_price(url):
    html = url_to_html(url)
    content_html_page = BeautifulSoup(html, 'html.parser')
    book_price = content_html_page.find_all(
        'span', class_="a-size-base a-color-price a-color-price")
    kindle_unlimited_price = get_kindle_unlimited_price(soup_html)
        'span', class_="extra-message olp-link")

    if (book_price):
        return get_formatted_price(str(book_price))

    if (kindle_unlimited_price):
        return get_formatted_price(str(kindle_unlimited_price))

    return False


def send_push_notification(url, preco_original, preco_ideal, push_option):
    # preco_atual = get_price(url)
    preco_atual = 0

    if preco_atual <= preco_ideal:
        print("Corre lá pra comprar!")
        return

    if (preco_atual < preco_original) and (push_option == True):
        print("O preço caiu")
        return

    return False


def main():
    invalid_value = None

    url = input("Cole abaixo a URL do livro físico ou eBook escolhido:")
    preco_original = get_price(url)

    if (type(preco_original) == float) or (type(get_price) == bool):
        print("O preço atual do produto é:", preco_original)
        while !((preco_ideal != invalid_value) and (preco_ideal < preco_original)):
            preco_ideal = float(
                input("Qual preço você quer pagar por esse produto?"))
    else:
        print("Não consegui encontrar o produto.")
        return

    # push_option = bool(input("Gostaria de receber...mesmo se..."))
    # send_push_notification(url, preco_original, preco_ideal, push_option)


main()
