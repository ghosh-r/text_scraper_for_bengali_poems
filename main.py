from typing import List
from sys import argv

from tqdm import tqdm
from time import sleep
from random import uniform

from bs4 import BeautifulSoup
import requests

from get_pages_urls import get_list_pages
from get_urls import get_urls_per_page
from write_poem import write_poem

def main(root_url: str,
         poet_url: str,
         text_file: str
         ) -> None:
    
    poems_list_pages = get_list_pages(root_url=root_url, poet_url=poet_url)
    
    poem_pages = [get_urls_per_page(page) for page in poems_list_pages]

    INDIV_POEM_URLS = []

    for url_group in poem_pages:
        for url in url_group:
            INDIV_POEM_URLS.append(url)
    
    for indiv_poem_url in tqdm(INDIV_POEM_URLS):
        random_sleep_sec = uniform(0, 5)
        sleep(random_sleep_sec)
        write_poem(url=indiv_poem_url, text_file=text_file)

    return


if __name__ == '__main__':
    main(root_url=argv[1], poet_url=argv[2], text_file=argv[3])