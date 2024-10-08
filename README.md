# Minddistrict Delegated Logon
Using Delegated Logon (“DLO”), a user can click on a URL that will log in the user into the Minddistrict platform. The DLO URL for a user can be generated using this small [Flask](https://flask.palletsprojects.com/en/3.0.x/) app. A user is authenticated using credentials and parameters that are encoded into the URL using [HMAC](https://en.wikipedia.org/wiki/HMAC).
For more information, see the [Minddistrict documentation.](https://docs.minddistrict.com/delegatedlogon/index.html)
### Features:

 - Generates a DLO URL for a client or care provider
 - Ability to select a path to the Minddistrict platform (optional)
 - Command-line and web-based interface available
 - Uses SHA-512 algorithm

### Installation:

 1. Make sure Python (3.12) and Flask (3.0.3) are installed. Next, setup and activate a virtual environment:
    
      `python -m venv .venv `

      `.\.venv\Scripts\activate`

 2. Install dependencies:
   
    `pip install -r requirements.txt`
 1. Create a *.env* file and add a secret key and a base URL:
   
    ` BASE_URL="https://example.minddistrict.dev/"   `  

    `DLO_SECRET=<YOUR SECRET KEY>`


### Usage:

Use the CLI by running:

`python dlo.py`

Or, use the web interface by running the Flask app:

`python app.py`

Enter a user ID and select 'client' or 'care-provider'. Optionally, provide a path in de Minddistrict platform to open once the user is logged in. Click submit to generate the DLO URL.
![DLO screenshot](dlo_screenshot.png)

### Tests:

To run a few unit tests for this project, run:

`pytest -v`