# test_wordcloud_generator.py

import unittest
from unittest.mock import patch, Mock
from fetch_text import fetch_text
from wordcloud_generator import wordcloud_generator
import numpy as np

class TestWordcloudGenerator(unittest.TestCase):

    @patch('requests.get')
    def test_fetch_text(self, mock_get):
        mock_get.return_value.text = 'Example Domain'
        text = fetch_text('http://www.example.com')
        # self.assertEqual(text, 'Example Domain')
        self.assertEqual(text, 'Example Domain')

    @patch('wordcloud_generator.WordCloud')
    @patch('matplotlib.pyplot.show')
    def test_wordcloud_generator(self, mock_show, mock_wordcloud):
        mock_wordcloud_instance = Mock()
        mock_wordcloud_instance.generate.return_value = np.zeros((100, 100))
        mock_wordcloud.return_value = mock_wordcloud_instance
        wordcloud = wordcloud_generator('Example Domain')
        mock_wordcloud.assert_called_once_with(
            random_state=8,
            normalize_plurals=False,
            width=600,
            height=300,
            max_words=300,
            stopwords=[]
        )
        mock_show.assert_called_once()

if __name__ == '__main__':
    unittest.main()