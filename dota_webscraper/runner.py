#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Runs package from beginning to end."""

import json
import os
import subprocess
import sys

from dota_spider import start_crawler as crawl
from gsheets_handle_stats import calc_requests
from upload_to_gsheets import upload_csv


def main():
    """
    Uses webcrawler to collect hero information, prompts user for requests, sets up
    csv files with embedded gsheets formulas, and exports csv files to gsheets.
    """

    filename = 'heroes.csv'

    # dota_spider.py
    crawl(filename)

    # client_interface.py
    #out = subprocess.check_output([sys.executable, './client_interface.py'])
    subprocess.check_output([sys.executable, './client_interface.py'])
    #print("out: {}".format(out))
    request_dict = {}
    with open('request.json', 'r') as f:
        request_dict = json.loads(f.read())

    # gsheets_handle_stats.py
    calc_filenames = calc_requests(filename, request_dict)

    # upload_to_gsheets.py
    upload_csv(calc_filenames)

    # removes all process files
    os.remove(filename)
    os.remove('request.json')
    for name in calc_filenames:
        os.remove(name)


if __name__ == '__main__':
    main()
