#!/bin/bash
echo Repository owner:
read repo_owner

repo_remote_name="${repo_owner}-origin"
repo_owner_and_name="${repo_owner}/datasets"
echo Adding remote...

add_remote() {
    dolt remote add $repo_remote_name "https://doltremoteapi.dolthub.com/${repo_owner_and_name}"
}


if ! add_remote; then
    echo The remote $repo_remote_name already exists. Would you like to continue \(yes\/no\)\? 
    read continue_with_existing_remote
fi

if [ $continue_with_existing_remote == "no" ]; then
    echo Please remove the existing remote and try again.
    exit 1
else
    echo Continuing with existing remote...
fi

echo Branch to review:
read repo_branch_to_review

dolt fetch repo_remote_name
dolt checkout  "${repo_remote_name}/${repo_branch_to_review}" "remotes/${repo_remote_name}/${repo_branch_to_review}"

echo Dolt committer:
read dolt_committer

if [ $dolt_committer == "" ]; then 
    echo Please provide the name of the committer
    exit 1
fi

echo Summary:
echo "Repository: ${repo_owner}"
echo "Remote: ${repo_remote_name}"
echo "Branch: ${repo_branch_to_review}"
echo "Checking out \`remotes/${repo_remote_name}/${repo_branch_to_review}\`"

echo Starting validation on ${dolt_committer}\'s changes to agencies.url...

find_invalid_urls() {
    keyword=$1;
    echo $keyword
    # WHERE COMMITTER NAME = AND DATE > 
    dolt sql -q "SELECT id, homepage_url FROM agencies WHERE homepage_url LIKE '%${keyword}%';"
}


while read line;
do find_invalid_urls $line
done < invalid_url_keywords.txt


# TODO: 
# for additions into agencies table, check for duplicates

# check for whitespaces in agencies.name
# also add check for whitespaces in all fields
# find_whitespaces() {
# SELECT name, CHAR_LENGTH(name), CHAR_LENGTH(TRIM(name)), committer, commit_hash, commit_date
# FROM `dolt_history_agencies`
# WHERE committer = "spacelove" AND  CHAR_LENGTH(name) != CHAR_LENGTH(TRIM(name));
# }

# SELECT count(id)
# FROM agencies
# WHERE LOWER(homepage_url) NOT LIKE '%pd%' AND
# LOWER(homepage_url) NOT LIKE '%police%' AND
# LOWER(homepage_url) NOT LIKE '%sheriff%' ANd
# LOWER(homepage_url) NOT LIKE '%lawenforcement%' AND
# LOWER(homepage_url) NOT LIKE '%law-enforcement%' AND
# LOWER(homepage_url) NOT LIKE '%safety%' AND
# LOWER(homepage_url) NOT LIKE '%marshal%' and
# LOWER(homepage_url) NOT LIKE '%criminal-justice%' AND
# LOWER(homepage_url) NOT LIKE '%criminaljustice%' AND
# LOWER(homepage_url) NOT LIKE '%attorney-general%' AND
# LOWER(homepage_url) NOT LIKE '%district-attorney%' AND
# LOWER(homepage_url) NOT LIKE '%districtattorney%' AND
# LOWER(homepage_url) NOT LIKE '%da%' AND
# LOWER(homepage_url) NOT LIKE '%attorneygeneral%' AND
# LOWER(homepage_url) NOT LIKE '%attorneygeneral%' AND
# LOWER(homepage_url) NOT LIKE '%so%' AND
# LOWER(homepage_url) NOT LIKE '%prosecutor%' AND
# LOWER(homepage_url) NOT LIKE '%sd%' AND
# LOWER(homepage_url) NOT LIKE '%sp%' AND
# LOWER(homepage_url) NOT LIKE '%department%'

# check no modifcations to date_insert
# SELECT diff_type, `from_id`, `to_id`, `from_name`, `to_name`, `from_date_insert`, `to_date_insert` FROM dolt_diff_agencies WHERE from_commit="i6ut64vj3p77o6jf3505g8l403h77mm8" AND to_commit="5b9fak0c0g891ftd87ec72jo20oi6m5f" AND from_date_insert != to_date_insert;