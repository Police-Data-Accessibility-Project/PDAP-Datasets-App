# When to use this
If you're reviewing a Pull Request (PR) in the [Datasets database](https://www.dolthub.com/repositories/pdap/datasets/doc/master), or want to speed up a review, **run these scripts and comment the results on the PR.**

These scripts are set up to assume that you set up your DoltHub database in the databases folder, like so: `PDAP-app/databases/datasets` . The script is assumed to live in the git repo directory. So, you may need to modify it for your workflow.

# Script explanations
## check_urls.py
The check_urls.py script is for testing if the URL is valid and exists. So, it'll first check if the URL looks valid (so, detecting stuff like https://example.com/, https://example2.com). After it passes that, it then tries the URL to see if it gets anything other than a 200 (Success), 301 (Permanent Redirect), or 302 (Temporary Redirect). If it does find any issues such as not having the right status code, timing out, or failing the URL validation, then it gets logged to a CSV with the reason why it failed.

We use GET requests because some servers act strangely or just break when using HEAD requests.

## domain_counter.py
domain_counter.py takes all the URLs and counts how many times each domain shows up. If it shows up more than once, it will be printed to the terminal in order of most used to least used domains. I wrote this script to help me find which domains may need to be banned.

## fix_spaces.py
fix_spaces.py will take the original CSV and remove leading and trailing spaces. After that, it'll go and remove anywhere there's more than one space for. So this ​​​​​​​​​​​​​​​​​​​     here (for some odd reason, Github will just remove the extra spaces I'm trying to put in my example, so I added some irregular whitespace characters to make it work) will turn into this here. 
