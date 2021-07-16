from typing import List

from bs4 import BeautifulSoup
import requests

def get_urls_per_page(url: str) -> List[str]:
    """
    inputs::
    url of a page containing many poems from one author -> str

    outputs::
    a list of str of urls

    returns::
    a list of str of urls -> list
    """
    list_of_urls = []
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    tds = soup.find_all('td')
    for td in tds:
        metas = td.find_all('meta', itemprop="url")
        for meta in metas:
            list_of_urls.append(meta.get('content'))
    return list_of_urls