# fetch_text.py

import requests
from bs4 import BeautifulSoup

def fetch_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return ' '.join(soup.stripped_strings)
