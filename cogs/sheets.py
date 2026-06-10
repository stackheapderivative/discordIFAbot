import gspread
from google.oauth2.service_account import Credentials

# scopes are the different accesses we can have
scopes = ["ENTER SCOPE HERE"]

creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
# auth ourself
client = gspread.authorize(creds)
# access id of google sheet
sheet_id = ""  # NOTE: GET ID OF SHEET, IT IS after d/ and before /edit.
# open spreadsheet
sheet = client.open_by_key(sheet_id)
# key is more foolproof since it uses just the id, prevents issue with name change.

# from sheet, on sheet1, it gets row values from row 1 and prints it.
values_list = sheet.sheet1.row_values(1)
print(values_list)
