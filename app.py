import os
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()


# TODO send push notification

KINDLE = os.getenv('KINDLE')


def isAmazonURL(url):
    return url.find("https://www.amazon.com") != -1


def url_to_html(url):
    validAmazonURL = isAmazonURL(url)

    if not validAmazonURL:
        return False
    try:
        req = Request(url)
        response = urlopen(req)
        return response.read()
    except HTTPError as e:
        print(e.status, e.reason)
    except URLError as e:
        print(e.reason)


def url_to_soup(url):
    html = url_to_html(url)

    if html:
        return BeautifulSoup(html, 'html.parser')
    return None


def parse_price(price):
    price_start = price.find('$') + 1
    price_end = price.find(',') + 3
    price = price[price_start:price_end]
    price = price.replace('.', '')
    price = price.replace(',', '.')
    return float(price)


def get_book_price(soup_html):
    return soup_html.find(
        'span', class_="a-size-base a-color-price a-color-price")


def get_kindle_unlimited_price(soup_html):
    return soup_html.find(
        'span', class_="extra-message olp-link")


def get_price(soup_html):
    book_price = get_book_price(soup_html)
    kindle_unlimited_price = get_kindle_unlimited_price(soup_html)

    if (book_price):
        return parse_price(str(book_price))

    if (kindle_unlimited_price):
        return parse_price(str(kindle_unlimited_price))

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
    # invalid_value = None
    # invalid_url = -1

    # url = input("Cole abaixo a URL do livro físico ou eBook escolhido:")
    # url = KINDLE
    url = "https://www.amazon.com/product"
    soup = url_to_soup(url)
    if soup:
        preco_original = get_price(soup)
        print("O preço original é:", preco_original)
    else:
        print("Algo deu errado :(")

    # if (type(preco_original) == float) or (type(get_price) == bool):
    #     print("O preço atual do produto é:", preco_original)
    #     while not((preco_ideal != invalid_value) and (preco_ideal < preco_original)):
    #         preco_ideal = float(
    #             input("Qual preço você quer pagar por esse produto?"))
    # else:
    #     print("Não consegui encontrar o produto.")
    #     return

    # push_option = bool(input("Gostaria de receber...mesmo se..."))
    # send_push_notification(url, preco_original, preco_ideal, push_option)


main()
