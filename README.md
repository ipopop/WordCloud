# Wordcloud Generator 🌐🖼️

This is a Python project that generates a word cloud from a webpage. The project follows the principles of clean architecture and uses a three-step TDD approach.

## Table of Contents 📚

- [Wordcloud Generator 🌐🖼️](#wordcloud-generator-️)
  - [Table of Contents 📚](#table-of-contents-)
  - [Installation 📦](#installation-)
  - [Clean Architecture 📚](#clean-architecture-)
  - [Test-Driven Development (TDD) 🧪](#test-driven-development-tdd-)
  - [Execution 🏃‍♀️](#execution-️)
    - [Running Tests](#running-tests)
    - [Running the Application](#running-the-application)
  - [Contributing 🤝](#contributing-)
  - [License 📄](#license-)

## Installation 📦

To install the necessary dependencies, run the following command:

```bash
pip3 install -r requirements.txt
```

## Clean Architecture 📚

The project is divided into three layers: the domain layer, the application layer, and the infrastructure layer.

- The application layer contains the `fetch_text.py` file, which fetches the text from a webpage, and the `create_wordcloud.py` file, which creates a word cloud from a string of text.
- The infrastructure layer is handled by the `requests` and `BeautifulSoup` libraries, which are used to fetch the webpage and parse the HTML, respectively.

## Test-Driven Development (TDD) 🧪

The project uses a three-step TDD approach:

1. Write a failing test. 🚫
2. Write the code to make the test pass. ✅
3. Refactor the code to improve its design and readability. 🔄

The tests are written using the `unittest` module in Python and are located in the `test_wordcloud_generator.py` file.

## Execution 🏃‍♀️

### Running Tests

To run the tests, navigate to the directory containing the `test_wordcloud_generator.py` file and run the following command:

```bash
python3 -m unittest test_wordcloud_generator.py
```

### Running the Application

To run the application, navigate to the directory containing the `main.py` file and run the following command:

```bash
python3 main.py
```

You will be prompted to enter the URL of the webpage you want to analyze. The project will then fetch the text from the webpage, tokenize the text, and create a word cloud from the tokens.

## Contributing 🤝

If you would like to contribute to the project, please follow the TDD approach and create a pull request with your changes.

## License 📄

This project is licensed under the MIT License.
