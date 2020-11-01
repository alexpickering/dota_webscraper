#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Prompts user input, parses into a dictionary of heroes and corresponding levels """

import json
import os
import re
import sys

from argparse import ArgumentParser
from gooey import Gooey, GooeyParser


def import_hero_list():
    # import hardcoded hero_list
    hero_list = []
    with open('hero_list.txt', 'r') as f:
        hero_list = [line.rstrip('\n') for line in f]
    return hero_list


def format_request(heroes, all_lvl):
    # regex separates entries into  hero,lvl tuples
    reg_obj = re.findall(r'([A-Za-z]+)([^A-Za-z]+)', heroes)

    hero_list = import_hero_list()

    outdict = {}
    for pair in reg_obj:
        # if multiple matches, takes first match (alphabetical)
        hero = [listhero for listhero in hero_list if pair[0] in listhero.lower()][0]

        lvls = []
        for elt in pair[1].split(','):
            print(elt)
            if '-' in elt:
                start, end = elt.split('-')
                start = int(start.strip())
                end   = int(end.strip())
                lvls += [lvl for lvl in range(start, end+1)]
            elif elt.strip():
                lvls.append(int(elt.strip()))
        outdict[hero] = lvls

    outdict['All Heroes'] = all_lvl

    # saving dictionary as file
    #with open('outdict.json','w+') as f:
    #    json.dump(outdict,f)

    print(outdict)
    return outdict


@Gooey
def set_gooey():
    pass


def main():
    if len(sys.argv) == 1:
        set_gooey()

    parser = ArgumentParser()
    parser.add_argument('hero', action='extend', type=str,  nargs='+', help='Hero and Level')
    parser.add_argument('--all', action='store', default=1, type=str, help='Level for All-Heroes Display')
    args = parser.parse_args()
    heroes = args.hero
    all_lvl = args.all

    req = format_request(' '.join(heroes), all_lvl)

    with open('request.json', 'w') as f:
        json.dump(req, f)

    #return req

if __name__ == '__main__':
    main()
