# wordcloud_generator.py

from wordcloud import WordCloud
import matplotlib.pyplot as plt

def wordcloud_generator(text):
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
    
    return wordcloud