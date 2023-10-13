import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def fetch_text(url):
    '''
    This function returns the text of a webpage
    given a URL
    '''

    # send a request to the webpage
    response = requests.get(url)

    # parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # extract the text and return it
    return ' '.join(soup.stripped_strings)

# Call the function with the URL of the webpage you want to analyze
url = input("Please enter the URL of the webpage you want to analyze: ")
text = fetch_text(url)

# Create the word cloud
wordcloud = WordCloud(
    random_state = 8,
    normalize_plurals = False,
    width = 600,
    height= 300,
    max_words = 300,
    stopwords = []
).generate(text)

# Create a figure
fig, ax = plt.subplots(1,1, figsize = (9,6))

# Add the word cloud to the figure
ax.imshow(wordcloud, interpolation='bilinear')

# Remove the axis
ax.axis("off")

# Display the figure
plt.show()


