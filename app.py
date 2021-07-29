from urllib.request import urlopen
from bs4 import BeautifulSoup


def url_to_html(url):
    response = urlopen(url)
    return response.read()


def find_price_in_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(id="kindle-price").get_text()


def get_formatted_price(price):
    idx_comma_price = str(price).find(',') - 2
    price = price[idx_comma_price:idx_comma_price+5]
    price = price.replace(',', '.')
    return float(price)

# TODO Errors validations


url = 'https://www.amazon.com.br/Fundacao-Funda%C3%A7%C3%A3o-Livro-Isaac-Asimov-ebook/dp/B015EECZDQ/?_encoding=UTF8&pd_rd_w=H2r79&pf_rd_p=83e1cfc7-91c9-4ba1-9a0a-5aa9ec7c1fae&pf_rd_r=W33P3XH7B63QSFK18W4T&pd_rd_r=7d4a931d-815a-420c-b2a3-923a59dc7715&pd_rd_wg=zzLGL&ref_=pd_gw_qpp'

# Main App
html = url_to_html(url)
price = find_price_in_html(html)
price = get_formatted_price(price)
print(type(price))
print(price)
