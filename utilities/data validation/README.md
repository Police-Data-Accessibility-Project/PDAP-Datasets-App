# Review steps for the `agencies` table: 
## Inspecting additions
In this case I found 8 additions that were duplicates due to a whitespace issue. I requested the user resolve the whitespace issue for these 8 rows. Now there are no additions in the PR, only modifications. You can filter pull request diffs by diff type ("Added", "Modified" or "Removed") on the [Pull request diff page](https://www.dolthub.com/repositories/pdap/datasets/pulls/43/compare). You should now see that there are no additions to the pull request. 
Additions to the `agencies` table will be few and easily reviewable. If there is an addition, I inspect the data to verify there are not unintended duplicates. 

### Using "Sonoma County Police Agency" as an example:
- SELECT * FROM agencies WHERE LOWER(name) LIKE '%sonoma%
- Verifying homepage_url's
  There were 13,999 rows modified in this PR. A few of us collaborated on a list of expected keywords in the homepage_url's (see `valid_homepage_url_keywords.txt` attached). Using those keywords I check for any homepage_url's that do not contain any of these keywords. [Here is the query](https://www.dolthub.com/repositories/spacelove/datasets/query/agencies-2?q=SELECT+id%2C+name%2C+homepage_url%0AFROM+agencies%0AWHERE+LOWER%28homepage_url%29+NOT+LIKE+%27%25pd%25%27+AND%0ALOWER%28homepage_url%29+NOT+LIKE+%27%25police%25%27+AND%0ALOWER%28homepage_url%29+NOT+LIKE+%27%25sheriff%25%27+ANd%0ALOWER%28homepage_url%29+NOT+LIKE+%27%25lawenforcement%25%27+AND%0ALOWER%28homepage_url%29+NOT+LIKE+%27%25law-enforcement%25%27+AND%0ALOWER%28homepage_url%29+NOT+LIKE+%27%25safety%25%27+AND%0ALOWER%28homepage_url%29+NOT+LIKE+%27%25marshal%25%27+and%0ALOWER%28homepage_url%29+NOT+LIKE+%27%25criminal-justice%25%27+AND%0ALOWER%28homepage_url%29+NOT+LIKE+%27%25criminaljustice%25%27+AND%0ALOWER%28homepage_url%29+NOT+LIKE+%27%25attorney-general%25%27+AND%0ALOWER%28homepage_url%29+NOT+LIKE+%27%25district-attorney%25%27+AND%0ALOWER%28homepage_url%29+NOT+LIKE+%27%25districtattorney%25%27+AND%0ALOWER%28homepage_url%29+NOT+LIKE+%27%25da%25%27+AND%0ALOWER%28homepage_url%29+NOT+LIKE+%27%25attorneygeneral%25%27+AND%0ALOWER%28homepage_url%29+NOT+LIKE+%27%25attorney-general%25%27+AND%0ALOWER%28homepage_url%29+NOT+LIKE+%27%25so%25%27+AND%0ALOWER%28homepage_url%29+NOT+LIKE+%27%25prosecutor%25%27+AND%0ALOWER%28homepage_url%29+NOT+LIKE+%27%25sd%25%27+AND%0ALOWER%28homepage_url%29+NOT+LIKE+%27%25sp%25%27+AND%0ALOWER%28homepage_url%29+NOT+LIKE+%27%25department%25%27&active=Tables) on spacelove's branch. 109 rows have a `homepage_url` that doesn't match any keywords (about 0.01% of the rows modified). Next I manually inspect a handful of those 109 rows to see if they're valid (the link clicks through and references the appropriate department).
- Attached you will also find `invalid_url_keywords` which I used to look for any `homepage_url`'s that contained any of those websites or keywords, and there were none.
- Removing whitespaces
[Query system table `dolt_history_agencies`](https://www.dolthub.com/repositories/spacelove/datasets/query/agencies-2?q=SELECT+name%2C+CHAR_LENGTH%28name%29%2C+CHAR_LENGTH%28TRIM%28name%29%29%2C+committer%2C+commit_hash%2C+commit_date%0AFROM+%60dolt_history_agencies%60%0AWHERE+committer+%3D+%22spacelove%22+AND++CHAR_LENGTH%28name%29+%21%3D+CHAR_LENGTH%28TRIM%28name%29%29%3B&active=Tables) to find the rows that spacelove modified that still have a whitespace. They then pushed a fix for these 114 rows.
- No changes to date_insert (unless there are additions)
[Query system table `dolt_diff_agencies`](https://www.dolthub.com/repositories/spacelove/datasets/query/agencies-2?q=SELECT+diff_type%2C+%60from_id%60%2C+%60to_id%60%2C+%60from_name%60%2C+%60to_name%60%2C+%60from_date_insert%60%2C+%60to_date_insert%60+FROM+dolt_diff_agencies+WHERE+from_commit%3D%22i6ut64vj3p77o6jf3505g8l403h77mm8%22+AND+to_commit%3D%225b9fak0c0g891ftd87ec72jo20oi6m5f%22+AND+from_date_insert+%21%3D+to_date_insert%3B&active=Tables) to see if spacelove changed any `date_insert`s (he did, but then reverted the changes since it refers to date inserted not date modified).
Modifications to location fields (lat, lng, city, state, county_fips)
- I manually spot checked some of these and they were correct. I also agreed with the participant's reasoning (this is pasted from the PR description):
"Some lat/lng pairs were overwritten, using the data from the exact location I pulled.  I needed lat/lng anyway to get the other location information, so I put it in the chart, even if it differed only slightly from the original. This seemed more fair than doing any arbitrary difference calculation, or keeping the previous lat/lng but then using my city/state/county_fips that may or may not be consistent with it. Finally,  @pdap-ericturner mentioned that they were scraped in any case, so I went with mine, since I felt they were as accurate or more."

Given that review, I think the pull request is ready to be merged. Let me know if you have any feedback or questions. If anyone is interested, you can check out the hacky bash script I wrote to automate the review process (see `validate_agencies_table.sh`). It's still a work in progress, but the steps are essentially:

1) Add remote of user's repo
2) Checkout remote branch
3) Validate that `homepage_url`'s do not contain invalid keywords.

Next steps: 
Merge PR #43 and review a couple more bounty PR's today
Translate my hacky bash script to python and add more test cases
Follow up with another example PR and steps to review `datasets` table
