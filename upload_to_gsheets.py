#!/usr/bin/env python3
import argparse
import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", type=str, help="The input csv file")
    args = parser.parse_args()

    credentials = ServiceAccountCredentials.from_json_keyfile_name('.dota-scraper-creds.json', scope)
    client = gspread.authorize(credentials)

    spreadsheet = client.open('DotA 2 Hero Stats')

    with open(args.csv, 'r') as file_obj:
        content = file_obj.read()
        client.import_csv(spreadsheet.id, data=content)


if  __name__ == '__main__':
    main()
