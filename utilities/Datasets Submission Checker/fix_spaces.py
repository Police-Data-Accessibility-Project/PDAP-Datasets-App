# I'm releasing this code under Public Domain (or Unlicense if your country doesn't have Public Domain) -- Alexis

import pandas as pd
import os

working_dir: str = "working"
dataset: str = os.path.join(working_dir, "datasets")
csv_file: str = os.path.join(dataset, "spaces-agencies.csv")
e_csv_file: str = os.path.join(dataset, "fixed-spaces-agencies.csv")

if __name__ == "__main__":
    df: pd.DataFrame = pd.read_csv(csv_file, dtype={'county_fips': object, 'zip': object})
    df2: pd.DataFrame = df.copy(deep=True)

    print("Original DataFrame:")
    print(df)

    # This'll strip off any leading and trailing spaces on every column that's a string type
    for (columnName, columnData) in df.iteritems():
        try:
            df2[columnName] = df2[columnName].map(lambda x: x.strip())
        except Exception:
            pass

    # This'll replace any extraneous spaces with a single space (e.g. `this   here` -> `this here`)
    df2 = df2.replace(to_replace=r'\s+', value=' ', regex=True)

    print("Fixed DataFrame:")
    print(df2)
    df2.to_csv(e_csv_file, index=False)

    # This is a hack for an experiment, do NOT use this!!!
    # df2["homepage_url"] = '""'
    # df2.to_csv(e_csv_file, index=False, quotechar=None, quoting=csv.QUOTE_NONE)
    # print(df2["homepage_url"])