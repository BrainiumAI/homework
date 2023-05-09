import os
import json
import sys
import pytest
from slugify import slugify

def save_scraped_data(output_folder, filename, data):
    filepath = os.path.join(output_folder, f"{filename}.txt")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(data)

def main():
    with open("settings.json", "r") as f:
        settings = json.load(f)

    output_folder = settings["output_folder"]
    os.makedirs(output_folder, exist_ok=True)

    for url_info in settings["urls_to_scrape"]:
        url = url_info["url"]
        expected_title = url_info["expected_title"]

        print(f"Scraping URL: {url}")

        exit_code = pytest.main(["-k", f"url_navigation[{url}]"])
        if exit_code != 0:
            sys.exit(exit_code)

        exit_code = pytest.main(["-k", f"page_title[{url}, {expected_title}]"])
        if exit_code != 0:
            sys.exit(exit_code)

        # Replace the following line with the actual scraping logic
        # that returns the page title or any other relevant text
        scraped_title = expected_title

        # Create a filename from the scraped title and save the data
        filename = slugify(scraped_title, max_length=50)
        save_scraped_data(output_folder, filename, scraped_title)

if __name__ == "__main__":
    main()
