# I'm releasing this code under Public Domain (or Unlicense if your country doesn't have Public Domain) -- Alexis

from validator_collection import validators, checkers, errors
from urllib.parse import urlparse

import pandas as pd
import requests
import csv
import os

working_dir: str = "working"
dataset: str = os.path.join(working_dir, "datasets")
csv_file: str = os.path.join(dataset, "urls.csv")
e_csv_file: str = os.path.join(working_dir, "url-errors.csv")

if __name__ == "__main__":
    df: pd.DataFrame = pd.read_csv(csv_file, dtype={'url': str})
    urls: list = df["url"].unique().tolist()

    error_log_handle = open(e_csv_file, mode="w")
    error_log: csv.writer = csv.writer(error_log_handle)

    error_log.writerow(["url", "reason", "status_code", "other_info"])

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }

    total_urls: int = len(urls)
    current_count: int = 1
    for url in urls:
        # print(url)
        # print(urlparse(url=url))
        # print(checkers.is_url(url))

        try:
            # Validate The URL
            validators.url(url)

            response: requests.Response = requests.get(url=url, headers=headers, timeout=30)

            if response.status_code != 200 and response.status_code != 301 and response.status_code != 302:
                print(f"{current_count}/{total_urls} - {url} - {response.status_code}")
                error_log.writerow([url, "Status Code", response.status_code, None])
        except errors.InvalidURLError:
            print(f"{current_count}/{total_urls} - Invalid URL: {url}")
            error_log.writerow([url, "Invalid URL", None, None])
        except Exception as e:
            print(f"{current_count}/{total_urls} - Error: {url}")
            error_log.writerow([url, "Unknown Error", None, str(e)])

        current_count += 1

        if current_count % 50 == 0:
            print(f"{current_count}/{total_urls} - Status Update Reminder - On URL: {url}")
