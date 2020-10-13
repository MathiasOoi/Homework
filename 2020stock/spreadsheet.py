import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)


class Sheet:
    def __init__(self):
        self.spreadsheet = client.open("stock2020")
    def createNewWkst(self, title, rows, cols):
        self.spreadsheet.add_worksheet(title=title, rows=rows, cols=cols)




