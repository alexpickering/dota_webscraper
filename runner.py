#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from dota_spider import start_crawler as crawl 
from gsheets_handle_stats import calc_requests
from upload_to_gsheets import upload_csv
import json
import subprocess
import sys

def main():
    
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

    # handle_stats.py
    filenames = calc_requests(filename, request_dict)
    
    # upload_to_gsheets.py
    upload_csv(filenames)


if __name__ == '__main__':
    main()
