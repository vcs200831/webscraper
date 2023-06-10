# Web Scraper

This is a Python project that scrapes data from IMDB's Top Rated Movies page and saves it in a CSV file.

## Features

- Uses requests and BeautifulSoup libraries to send HTTP requests and parse HTML documents
- Extracts the title, year, and rating of the top 250 movies from IMDB
- Writes the data in a CSV file with proper headers and formatting
- Handles exceptions and errors gracefully

## Requirements

- Python 3.7 or higher
- requests 2.26.0 or higher
- BeautifulSoup 4.10.0 or higher

## Installation

To install the required libraries, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To run the web scraper, run the following command:

```bash
python scraper.py
```

The output will be a CSV file named "movies.csv" in the same directory as the script.

