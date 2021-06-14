# PDAP App
A set of tools to help data scrapers collect and submit data.

## Getting Started
1. Clone this repo and `cd` into the directory
2. If you're working with DoltHub repos, install them in `/databases`.

### To use the Django app, continue:

3. Have Python, PIP & virtualenv installed
4. Create a venv (`python -m "venv" ./env`)
    * To activate on windows, you will run `.\\env\Scripts\activate.ps1` or `.\env\Scripts\activate.bat`
    * To activate on *nix, `. ./venv/bin/activate`
5. In your venv, grab all the requirements: `pip install -r requirements.txt`
6. Now you can `cd pdap` and interact with the `manage.py` file:
    * `python manage.py` will show all the available commands
    * `python manage.py makemigrations` is useful when any of the models.py files are updated (to actually create a migration to sync to DB)
    * `python manage.py runserver` will run a dev version for you (needs an .env file with a testing PostgreSQL db running)

# Explanations
## /pdap
The Django app.

## /utilities
Scripts for scrapers and dataset maintenance.
