#!/usr/bin/env python3
import argparse
import csv
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

    # temporarily commented out: upload overwrites formatting
    # Upload part
    with open(args.csv, 'r') as file_obj:
        edited_file_obj = edit_data(file_obj)
        content = edited_file_obj.read()
        client.import_csv(spreadsheet.id, data=content)


    sh = spreadsheet.sheet1

    # TODO(apick): 
    # 1. cull headers
    # 2. make lvl-dependent stats via formulas

    # B1:AE1 = lvl request cells
    # starts = [ (x * 119) + 3 for x in range(29) ]
    # ends   = [ (x * 119) + 121 for x in range(29) ]
    # per_lvl_blocks = [str(x) + ':' + str(y) for x, y in zip(starts, ends)]
    




    # formatting cells
    sh.format('A1:BQ1', {'textFormat': {'bold': True}})
    sh.sort((1, 'asc'), range='A2:BQ120')


def edit_data(csvfile):
    csvreader = csv.reader(csvfile)




if  __name__ == '__main__':
    main()
