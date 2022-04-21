[![codecov](https://codecov.io/gh/amakarudze/xmlreader/branch/main/graph/badge.svg?token=IjTttuyMoe)](https://codecov.io/gh/amakarudze/xmlreader)

# xml-to-html converter

This is an app for converting DMARC XML files to JSON that is presented on HTML file for readability. We have recently added DMARC policy to the [djangogirls.org](https://djangogirls.org/) domain to prevent spammers from using our domain to send phishing emails via [Sendgrid](https://sendgrid.com/) that appear to be coming from [hello@djangogirls.org](hello@djangogirls.org) or  [fundraising@djangogirls.org](fundraising@djangogirls.org) email addresses. 

DMARC reports are being sent to our `dmarc` email address. Analyzing these emails hasn't been easy as they only contain `XML` files which are not human-readable. Since the DMARC rules have kind of broken some of our email functionality on the website, I needed a way to decode the DMARC reports attachments so we can adjust our DMARC rules - and this is how this app came to be.

## Installation
### Requirements
* Python 3.9 +
* Django 4.0 +
* Postgres 12

### Setting up
* Clone this repo.
* Create a virtual envinronment on your machine.
* Run `pip install -r requirements.txt` to install required packages.
* Create a local Postgres database.
* Run `python manage.py migrate` to run migrations.

## Testing
To test using automated tests, run:

coverage run -m pytest

## Usage
* Run `python manage.py runserver` to run the project and open `http://127.0.0.1:8000/`.
* Upload a DMARC file and yay you're all set!
