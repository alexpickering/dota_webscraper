#!/usr/bin/env python3
import argparse
import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from handle_stats import calc_lvl_stats


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


    #calc_lvl_stats(args.csv)
    #print(args.csv)

    # temporarily commented out: upload overwrites formatting
    # Upload part
    with open(args.csv, 'r') as file_obj:
        content = file_obj.read()
        client.import_csv(spreadsheet.id, data=content)


    sh = spreadsheet.sheet1

    # B1:AE1 = lvl request cells
    # starts = [ (x * 119) + 3 for x in range(29) ]
    # ends   = [ (x * 119) + 121 for x in range(29) ]
    # per_lvl_blocks = [str(x) + ':' + str(y) for x, y in zip(starts, ends)]
    




    # formatting cells
    sh.format('A1:BQ1', {'textFormat': {'bold': True}})
    sh.sort((1, 'asc'), range='A2:BQ120')



if  __name__ == '__main__':
    main()
