import requests
from bs4 import BeautifulSoup

def send_request(url):
    return requests.get(url)

def parse_page_content(text):
    return BeautifulSoup(text, 'html.parser')

def fetch_text(url):
    '''
    This function returns the text of a webpage
    given a URL
    '''

    # send a request to the webpage
    response = send_request(url)

    # parse the page content with BeautifulSoup
    soup = parse_page_content(response.text)

    # extract the text and return it
    return ' '.join(soup.stripped_strings)
