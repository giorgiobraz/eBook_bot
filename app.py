from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys


def eBook_price(kindle_price_in_html):
    index_price = kindle_price_in_html.find('$') + 2
    price = kindle_price_in_html[index_price:index_price+5]
    return price


def url_cleanup(url):
    idx_search = url.find('?') - 1
    return url[:idx_search]


url = 'https://www.amazon.com.br/Aprendendo-aprender-para-crian%C3%A7as-adolescentes-ebook/dp/B07N47KMGP/?_encoding=UTF8&pd_rd_w=bkn4w&pf_rd_p=4b9652c9-ac45-4535-ac4d-eec51129bb6c&pf_rd_r=ZYT0QCN9E93T8CEMCRDT&pd_rd_r=9ef4b2df-6c44-4b0f-940c-958fbc0f013b&pd_rd_wg=CeVBJ&ref_=pd_gw_ci_mcx_mr_hp_d'


# Abre, grava e trata a URL

# url = sys.argv[1]
# print(type(url))

url = url_cleanup(url)
# print(url)
response = urlopen(url)
html = response.read()
html = str(html)
html = " ".join(html.split())

# TODO Errors validations

# Busca preço do eBook no HTML
soup = BeautifulSoup(html, 'html.parser')
html_price_filter = soup.findAll(id="kindle-price")
html_price_filter = str(html_price_filter)
print(eBook_price(html_price_filter))

# print(sys.argv[1])
