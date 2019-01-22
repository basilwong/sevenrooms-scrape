from datetime import datetime
from datetime import timedelta

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

class SevenroomScraper:

    def __init__(self, email, password):
        """
        Opens chrome to scrape sevenroom.com.

        :param email: login email
        :param password: login password
        """
        self.user = email
        self.password = password
        self.date = datetime.today()

        self.driver = webdriver.Chrome()
        self.driver.get("https://www.sevenrooms.com/login")
        # Login
        self.driver.find_element_by_name("email").send_keys(email)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_name("lsubmit").click()

        self.update_html()

    def update_html(self):
        """
        Method used for updating the soup object when the webpage is changed.
        """
        self.html = self.driver.page_source
        self.soup = BeautifulSoup(self.html, features="lxml")

    def change_date(self, date):
        """
        There is a different webpage for each date. Changes the date so that clients that make reservations on different
        dates can be logged.

        :param date: date to change to
        """
        self.date = date
        relative_url = "https://www.sevenrooms.com/manager/twelvewest/reservations/day/" + date.strftime("%m-%d-20%y")
        self.driver.get(relative_url)
        self.update_html()

    def check_for_client(self):
        name_tag = self.client.find_all("span", {"class": "client-info-name"})
        return not name_tag

    def parse_client_html(self):
        """
        Given a client tag, parses information into a dictionary.

        :return: dictionary with client info
        """
        data = dict()
        data["date"] = self.date.strftime("%m-%d-20%y")
        name_tag = self.client.find_all("span", {"class": "client-info-name"})
        data["name"] = name_tag[0].text
        guests_tag = self.client.find_all("div", {"class": "col col-partysize number-fix"})
        data["guests"] = guests_tag[0].text
        min_tag = self.client.find_all("div", {"class": "col col-minimum"})
        data["min"] = min_tag[0].text
        table_tag = self.client.find_all("div", {"class": "col col-table-no ellipsis"})
        data["table"] = table_tag[0].text
        notes_tag = self.client.find_all("div", {"class": "is-mobile notes"})
        if notes_tag:
            data["notes"] = notes_tag[0].text
        else:
            data["notes"] = ""
        data["booked"] = self.client["sort_via"]
        return data

    def scrape_clients(self):
        """
        Scrape client information.

        :return: client information in a dictionary
        """
        client_list = list()

        actuals_list = self.soup.find_all(id="actuals-list")
        actuals_list = actuals_list[0]
        divs = actuals_list.find_all(recursive=False)

        for ui_divs in divs:
            if ~ui_divs.has_attr('class'):
                html_list = ui_divs.find_all(recursive=False)
                for client in html_list:
                    self.client = client
                    if not self.check_for_client():
                        client_list.append(self.parse_client_html())

        return client_list


    def __del__(self):
        self.driver.close()




