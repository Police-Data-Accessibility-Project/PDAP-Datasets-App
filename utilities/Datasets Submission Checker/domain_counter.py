# I'm releasing this code under Public Domain (or Unlicense if your country doesn't have Public Domain) -- Alexis

from urllib.parse import urlparse

import pandas as pd
import os

working_dir: str = "databases"
address_csv: str = os.path.join(working_dir, "datasets", "agencies.csv")
export_csv: str = os.path.join(working_dir, "datasets", "agencies_counter.csv")

df = pd.read_csv(address_csv)
df = df[~df["homepage_url"].isnull()]

urls = df["homepage_url"].unique().tolist()

counter: dict = {}
for url in urls:
    # This is to prevent confusing the URL Parser
    if "http://" not in url and "https://" not in url:
        url = f"http://{url}"

    host: str = urlparse(url).netloc.strip()
    if host not in counter:
        counter[host] = 1
    else:
        counter[host] += 1
        # print(host)

counter_df = pd.DataFrame.from_dict(counter, orient="index", columns=["count"])
counter_df = counter_df.sort_values(by='count', ascending=False)
counter_df = counter_df[counter_df["count"] != 1]

print(counter_df)
counter_df.to_csv(export_csv)
