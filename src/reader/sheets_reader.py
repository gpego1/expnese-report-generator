import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent.parent

filename = BASE_DIR / os.getenv("GOOGLE_DRIVE_CREDENTIALS_FILE")
scopes = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
credentials = Credentials.from_service_account_file(
    filename = filename,
    scopes = scopes
)

client = gspread.authorize(credentials)
entire_spreadsheet = client.open(
    title=os.getenv("GOOGLE_SPREADSHEET_TITLE"),
    folder_id=os.getenv("GOOGLE_SPREADSHEET_FOLDER_ID")
)

spreadsheet = entire_spreadsheet.get_worksheet(0)
spreadsheet_data = spreadsheet.get_all_records()


def read_spreadsheet():
    df = pd.DataFrame(spreadsheet_data)
    print(df.head())

read_spreadsheet()