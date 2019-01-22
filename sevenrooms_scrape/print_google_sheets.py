import gspread
from oauth2client.service_account import ServiceAccountCredentials

# https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html

class PrintToGoogleSheets:

    def __init__(self, sheet_name):
        """
        Sets up connection to specified google sheet. Requires json credential file.

        :param sheet_name: title of the google sheet to be edited
        """
        self.scope = ['https://spreadsheets.google.com/feeds' + ' ' + 'https://www.googleapis.com/auth/drive']
        self.creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', self.scope)
        self.client = gspread.authorize(self.creds)
        self.sheet = self.client.open(sheet_name).sheet1
        self.names_list = self.sheet.col_values(1)

    def list_from_dict(self, dict):

        ret = list()

        ret.append(dict["name"])
        ret.append(dict["guests"])
        ret.append(dict["min"])
        ret.append(dict["table"])
        ret.append(dict["notes"])
        ret.append(dict["booked"])
        ret.append(dict["date"])

        return ret

    def update_names_list(self):
        self.names_list = self.sheet.col_values(1)

    def add_clients(self, list_of_clients):
        for client in list_of_clients:
            if client["name"] not in self.names_list:
                row = self.list_from_dict(client)
                self.sheet.append_row(row)
                self.update_names_list()


if __name__ == "__main__":
    printer = PrintToGoogleSheets()
