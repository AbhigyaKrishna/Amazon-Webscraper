import json

from selectorlib import Extractor

from amazon import AmazonSession
from serialize import AmazonSearchResultEncoder


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
    result = [AmazonSearchResultEncoder.from_dict(r) for r in data['product']]

    with open("output.json", "w") as f:
        json.dump(result, f, cls=AmazonSearchResultEncoder)
    print("Output dumped to output.json")


if __name__ == '__main__':
    main()
