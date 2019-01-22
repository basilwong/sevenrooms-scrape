"""
Example code for using the SevenroomScraper and PrintToGoogleSheets. Scrapes a years worth of reservations and then
logs them to a google sheets document.
"""

from sevenrooms_scrape.sevenroom_scraper import SevenroomScraper
from sevenrooms_scrape.print_google_sheets import PrintToGoogleSheets
from datetime import datetime
from datetime import timedelta

if __name__ == "__main__":

    username = input("Login email: ")
    password = input("Login password: ")
    sheet_name = input("Google sheets title: ")

    scrpr = SevenroomScraper(username, password)
    printer = PrintToGoogleSheets(sheet_name)

    date = datetime.today()
    scrpr.change_date(date)

    for i in range(365):
        client_list = scrpr.scrape_clients()
        printer.add_clients(client_list)
        date = date - timedelta(days=1)
        scrpr.change_date(date)
