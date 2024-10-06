# Amazon Webscraper

A Python-based web scraper that uses **Selectorlib** to extract product information from Amazon, including product names, prices, ratings, and more. It provides a command-line interface (CLI) powered by **Typer**, and displays real-time progress using **Rich**.

## Features

- Extract product details (name, price, ratings, reviews)
- Save results to CSV or JSON
- Handles pagination to scrape multiple pages of results
- Easy-to-use CLI interface with Typer
- Real-time progress and beautiful terminal output using Rich
- Configurable scraping parameters (number of pages, search query, etc.)
- Error handling and rate-limiting to avoid detection by Amazon

## Installation

### Prerequisites

- Python 3.x
- [Selectorlib](https://pypi.org/project/SelectorLib/)
- [Requests](https://pypi.org/project/requests/)
- [Typer](https://typer.tiangolo.com/)
- [Rich](https://pypi.org/project/rich/)

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/amazon-webscraper.git
   ```
2. Navigate to the project directory:
   ```bash
   cd amazon-webscraper
   ```
3. Create and activate a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

#### Running the Scraper

To run the scraper for a specific search term, use:
```bash
python amazon_scraper.py "search_term"
```

Example:
```bash
python amazon_scraper.py "laptop"
```

Options:
```bash
--limit               INTEGER  [default: 10]                                                                                                                                                               │
--price               INTEGER  [default: None]                                                                                                                                                             │
--rating              FLOAT    [default: None]                                                                                                                                                             │
--review-count        INTEGER  [default: None]                                                                                                                                                             │
--discount            INTEGER  [default: None]                                                                                                                                                             │
--help                         Show this message and exit.
```

## Dependencies

The following libraries are used in this project:

* **Selectorlib**: For scraping and extracting structured data from Amazon pages using CSS selectors.
* **Requests**: For making HTTP requests to fetch Amazon pages.
* **Typer**: For building the command-line interface (CLI) of the scraper.
* **Rich**: For rich text formatting and progress bar visualization in the terminal.

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository
2. Create a new branch (git checkout -b feature-branch)
3. Commit your changes (git commit -am 'Add feature')
4. Push to the branch (git push origin feature-branch)
5. Open a Pull Request
