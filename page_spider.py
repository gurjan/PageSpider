import os
import argparse
from utilities import url_utilities
# Avoid ssl cert problem
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

def main(database: str, url_list_file: str):
    big_word_list = []
    print("we are going to work with: " + database)  # commad + D to duplicate previous line
    print("we are going to scan: " + url_list_file)
    urls = url_utilities.load_urls_from_file(url_list_file)
    for url in urls:
        print("Reading from " + url)
        page_content = url_utilities.load_page(url=url)  # url=url - explicit name
        words = url_utilities.scrape_page(page_contents=page_content)
        big_word_list.extend(words)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--database", help="SQLite File Name")
    parser.add_argument("-i", "--input", help="File containing urls to read")
    args = parser.parse_args()
    database_file = args.database
    input_file = args.input
    main(database=database_file, url_list_file=input_file)
