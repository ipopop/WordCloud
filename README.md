# WordCloud from URL 🌐

## Description 📝

This project is a Python application that generates a word cloud from the text content of a given webpage. The word cloud is generated using the WordCloud library in Python and is displayed using Matplotlib.

## Table of Contents 📚

- [Installation](#installation-)
- [Usage](#usage-)
- [Execution](#execution-)
- [TDD Steps](#tdd-steps-)
- [Contributing](#contributing-)
- [License](#license-)

## Installation 🛠️

To install the necessary dependencies, use the following command:

```bash
pip3 install requests BeautifulSoup4 wordcloud matplotlib
```

## Usage 📖

To use this application, simply input the URL of the webpage you want to analyze when prompted. The application will then fetch the webpage, extract the text content, and generate a word cloud.

## Execution 🚀

To run the tests, use the following command:

```bash
python3 -m unittest test_wordcloud
```

To run the script, use the following command:

```bash
python3 word_cloud.py
```

## TDD Steps 🧪

### Step 1: Red 🔴

First, we need to write a failing test for the fetch_text function. We can use the unittest module in Python to write our tests. Create a new file called `test_wordcloud.py` and write a test case for the `fetch_text` function.

### Step 2: Green 🟢

Next, we need to write code to make the test pass. In this case, the `fetch_text` function is already implemented in the `word_cloud.py` script, so we don't need to write any new code.

### Step 3: Refactor 🔄

Finally, we can refactor the `fetch_text` function to improve its structure and readability. For example, we can extract the creation of the `requests.get` object and the parsing of the page content into separate functions.

## Contributing 🤝

Contributions are welcome! Please feel free to submit a pull request or open an issue if you encounter any problems or have suggestions for improvement.

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
