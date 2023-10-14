import unittest
from WordCloud import fetch_text

class TestWordCloud(unittest.TestCase):
    def test_fetch_text(self):
        url = "https://example.com"
        text = fetch_text(url)
        self.assertIsNotNone(text)

if __name__ == '__main__':
    unittest.main()
