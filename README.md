# sevenrooms-scrape

Log your clients' data from sevenrooms.com by scraping directly from the website.

## Installation/Setup

``` git clone https://github.com/basilwong/sevenrooms_scrape.git ```

### Setting up chromedriver

Download [chromedriver](http://chromedriver.chromium.org/) and save it to the 
assets folder. 

### Setting up print_google_sheets

1. Go to [Google API Console](https://console.developers.google.com/)
2. Create new project
3. Click Enable API then enable the Google Drive API.
4. Create credentials for a Web Server to access Application Data.
5. Name the service account and grant it a Project Role of Editor.
6. Download JSON file.
7. Copy JSON file to the assets directory and rename: client_secret.json



