import gspread
from oauth2client.service_account import ServiceAccountCredentials

def authenticate_google_sheets():
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets']
    creds = ServiceAccountCredentials.from_json_keyfile_name('your-credentials.json', scope)
    client = gspread.authorize(creds)
    return client

def append_to_sheet(price, link):
    client = authenticate_google_sheets()
    spreadsheet = client.open('Rental Listings').sheet1
    spreadsheet.append_row([price, link])
