# main.py

from fetch_text import fetch_text
from wordcloud_generator import wordcloud_generator
import requests

while True:
    url = input("Please enter the URL of the webpage you want to analyze: ")
    try:
        text = fetch_text(url)
        wordcloud_generator(text)
        break
    except requests.exceptions.InvalidURL:
        print("URL is not valid, try again!")
