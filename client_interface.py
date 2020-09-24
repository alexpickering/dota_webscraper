from argparse import ArgumentParser
from gooey import Gooey, GooeyParser
import os
import re
import json
import sys


# TODO: clean up and pare down format_request
def format_request(heroes, all_lvl):
    print("parser output: ")
    print(heroes)
    raw_list = []

    print("regex split: ")
    print(re.split(',| ', ' '.join(heroes)))

    for elt in re.split(',| ', ' '.join(heroes)):
        if '-' in elt:
            start, end = elt.split('-')
            start = int(start.strip())
            end   = int(end.strip())
            raw_list += [lvl for lvl in range(start, end+1)]
        else:
            raw_list.append(elt)

    raw_list = list(filter(None, raw_list))

    print("raw_list: ")
    print(raw_list)

    # import hardcoded hero_list
    hero_list = []
    with open('hero_list.txt', 'r') as f:
        hero_list = [line.rstrip('\n') for line in f]
    num_list = list(range(1,31))
    rough_list= []

    for hero in raw_list:
        if isinstance(hero, int):
            rough_list.append(hero)
        else:
            rough_list += (listhero for listhero in hero_list if hero.lower() in listhero.lower())
            rough_list += (n for n in num_list if hero.isnumeric() and int(hero) == n)

    print("rough_list:")
    print(rough_list)

    deduped_list = []

    for elt in rough_list:
        if isinstance(elt, int) or elt not in deduped_list:
            deduped_list.append(elt)

    print("deduped_list:")
    print(deduped_list)


    out_dict = {}

    i = 0
    val_list = []
    list_length = len(deduped_list)
    while i < list_length:
        if i < list_length-1 and isinstance(deduped_list[i+1], int):
            hero_name = deduped_list[i]
            val_list.clear()
            while i < list_length-1 and isinstance(deduped_list[i+1], int):
                val_list.append(deduped_list[i+1])
                i = i + 1
                #print(val_list)
                #print("first while " + str(i))
            out_dict[hero_name] = sorted(val_list.copy())
            i = i + 1
            #print(out_dict)
            #print("second, after out_dict " + str(i))
        else:
            hero_name = deduped_list[i]
            out_dict[hero_name] = [1]
            i = i + 1
            #print("third, in else " + str(i))

    out_dict['All Heroes'] = all_lvl

    # saving dictionary as file
    #with open('out_dict.json','w+') as f:
    #    json.dump(out_dict,f)

    print(out_dict)
    return out_dict


@Gooey
def set_gooey():
    pass


def main():
    if len(sys.argv) == 1:
        set_gooey()

    parser = ArgumentParser()
    parser.add_argument('hero', action='extend', type=str,  nargs='+', help='Hero and Level')
    parser.add_argument('--all', action='store', default=1, type=str, help='Level for All-Heroes Display')
    #parser.add_argument('hero', choices=HERO_LIST)
    args = parser.parse_args()
    heroes = args.hero
    all_lvl = args.all

    print(len(sys.argv))
    print(sys.argv)

    req = format_request(heroes, all_lvl)

    with open('request.json', 'w') as f:
        json.dump(req, f)

    #return req

if __name__ == '__main__':
    main()
