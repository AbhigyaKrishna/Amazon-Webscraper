import json

from amazon import AmazonSession
from selectorlib import Extractor


def main():
    print("Starting Amazon Scraper")
    print("Initializing session...")
    session = AmazonSession()
    print("Session initialized")
    session.home()

    print("Searching for laptops...")
    res = session.search("laptop")
    print("Extracting data...")
    e = Extractor.from_yaml_file("search_result_selector.yml")

    data = e.extract(res.text)
    if data:
        with open('output.json', 'w') as out:
            json.dump(data, out, indent=4)
            out.write("\n")
    print("Output dumped to output.json")


if __name__ == '__main__':
    main()
