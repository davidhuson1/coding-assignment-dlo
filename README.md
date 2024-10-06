# Minddistrict Delegated Logon
Using Delegated Logon (“DLO”) a user can click a on URL that will login the user into the Minddistrict platform using the credentials encoded in this URL. The DLO URL's for user can be generated using this small [Flask](https://flask.palletsprojects.com/en/3.0.x/) app. A user is authenticated using their credentials and parameters that are encoded into the URL using [HMAC](https://en.wikipedia.org/wiki/HMAC).
For more information see the [Minddistrict documentation.](https://docs.minddistrict.com/delegatedlogon/index.html)
### Features:

 - Generates a DLO URL for a client or care provider
 - Ability to select a path to the Minddistrict platform (optional)
 - Command-line and web-based interface available
 - Uses SHA-512 algorithm

### Installation:

 1. Setup and activate a virtual environment:
    
      `python -m venv .venv `

      `.\venv\Scripts\activate`

 2. Install dependencies:
   
    `pip install -r requirements.txt`
 1. Create a *.env* file and add a secret key and a base URL:
 ` BASE_URL="https://example.minddistrict.dev/"   DLO_SECRET=<YOUR SECRET KEY> `


### Usage:

Use the CLI by running:

`python DLO.py`

Or, use the web interface by running the Flask app:

`python app.py`

