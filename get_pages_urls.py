from typing import List

from bs4 import BeautifulSoup
import requests

from time import sleep
from random import uniform

def get_list_pages(root_url: str, poet_url: str) -> List[str]:
    """
    inputs::
    root_url: root_url of the website -> str
    poet_url: root url of the poet, like rabindranath -> str

    outputs::
    a list of urls of pages containing links to multiple poems -> List(str)

    returns::
    page_urls: a list of urls of pages containing links to multiple poems -> List(str) 
    """
    html_text = requests.get(root_url + poet_url).text
    soup = BeautifulSoup(html_text, 'lxml')
    
    pages = soup.find_all('ul', class_='pagination')
    
    for page in pages:
        a_s = page.find_all('a')
        hrefs = [a.get('href') for a in a_s]

        
    last_page_n = int(hrefs[-1].split('=')[-1])
    page_urls = [root_url + poet_url + '?t=p&pp=' + str(i) for i in range(1, last_page_n+2)]

    return page_urls

if __name__ == '__main__':
    print(get_list_pages('https://www.bangla-kobita.com/', 'ishwarchandragupta/'))