from typing import List
from sys import argv

from bs4 import BeautifulSoup
import requests

def write_poem(url: str, text_file: str) -> None:
    """
    inputs::
    url of poem -> str
    path of text file -> str

    outputs::
    poem appended to text file

    returns::
    None -> None
    
    """
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    title = soup.find('h1').text
    author = soup.find('div', class_="author-name").text
    poem_html_formatted = soup.find('div', class_="post-content noselect")
    poem = poem_html_formatted.find_all('p')
    poem_str = ''
    for line in poem:
        poem_str += (str(line).replace('<p>', '').replace('</p>', '').replace('<br/>', '\n'))
    with open(text_file, 'a') as f:
        f.write(title + '\n\n' + poem_str + '\n\n\n\n')
    return