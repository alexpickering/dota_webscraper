#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Uploads Hero stats csv file(s) to Google Sheets "DotA 2 Hero Stats" spreadsheet."""

import argparse
import csv

import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"]


def upload_csv(filenames):
    credentials = ServiceAccountCredentials.from_json_keyfile_name('.dota-scraper-creds.json', scope)
    client = gspread.authorize(credentials)



    if type(filenames) == str:
        filenames = [filenames]

    # Upload
    i = 0
    for filename in filenames:
        spreadsheet = client.open('DotA 2 Hero Stats')
        worksheet = spreadsheet.get_worksheet(i)
        if worksheet == None:
            worksheet = spreadsheet.add_worksheet(title='sheet'+str(i+1), rows=130, cols=30,index=i)
        else:
            worksheet.clear()
        with open(filename, 'r') as file_obj:
            reader = csv.reader(file_obj)
            spreadsheet.values_update(
                    worksheet.title,
                    params={'valueInputOption': 'USER_ENTERED'},
                    body={'values': list(reader)}
            )
        i = i+1

        # formatting cells
        #spreadsheet.format('A1:BQ1', {'textFormat': {'bold': True}})
        #spreadsheet.sort((1, 'asc'), range='A2:BQ120')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", type=str, nargs='+', help="The input csv file")
    args = parser.parse_args()
    upload_csv(args.csv)


if  __name__ == '__main__':
    main()
