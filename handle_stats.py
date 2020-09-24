import csv
import copy
import json
from hero import Hero


def using_csv(filename):
    with open(filename, 'r') as f:
        raw = csv.DictReader(f)

        data = {}
        for elt in raw:
            data[elt['hero']] = elt
        del data['hero']

    return data


def get_request_dict(filename):
    with open(filename, 'r') as f:
        request_dict = json.loads(f.read())
    return request_dict


def calc_requested_heroes(hero_objs, request_dict):
    """Calculates stats for requested heroes in request dictionary."""
    outdict = {}
    for hero, lvls in request_dict.items():
        for lvl in lvls:
            hero_objs[hero].level = lvl
            hero_objs[hero].name = hero + '_' + str(lvl)
            outdict[hero + '_' + str(lvl)] = hero_objs[hero].to_dict(title_case=True, rounded=True)
            
    return outdict


def calc_all_heroes(hero_objs, request_lvl):
    """Calculates stats for all heroes at requested level."""
    outdict = {}
    for hero_name, hero in hero_objs.items():
        hero.level = int(request_lvl)
        outdict[hero_name] = hero.to_dict(title_case=True, rounded=True)
    return outdict


def values_to_instances(data):
    """Converts dictionary values to instances of Hero class."""
    hero_objs = {}
    for hero in data.keys():
        hero_objs[hero] = Hero(**data[hero])
    return hero_objs
    

def write_to_csv(outdict, filename):
    with open(filename, 'w') as csvfile:
        _, fieldnames = next(iter(outdict.items()))
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for hero_name, hero_dict in outdict.items():
            writer.writerow(hero_dict)


def calc_requests(filename, request_dict):
    data = using_csv(filename)
    hero_objs = values_to_instances(data)
 
    all_lvl = request_dict.pop('All Heroes', 1)

    filename_all = 'heroes_to_upload_all.csv'
    outdict_all = calc_all_heroes(hero_objs, all_lvl)
    write_to_csv(outdict_all, filename_all)

    filename_req = 'heroes_to_upload_req.csv'
    outdict_req = calc_requested_heroes(hero_objs, request_dict)
    write_to_csv(outdict_req, filename_req)

    return (filename_all, filename_req)


def main():
    test_filename = 'heroes.csv'
    test_request_dict = {'All Heroes': 15, 'Abaddon': [2,4,11], 'Lone Druid': [23,27,30], 'Axe': [1,3]}
    request_dict_filename = 'request.json'

    data = using_csv(test_filename)
    hero_objs = values_to_instances(data)
 
    #request_dict = get_request_dict(request_dict_filename)
    request_dict = test_request_dict
    all_lvl = request_dict.pop('All Heroes', 1)

    filename_all = 'heroes_to_upload_all.csv'
    outdict_all = calc_all_heroes(hero_objs, all_lvl)
    write_to_csv(outdict_all, filename_all)

    filename_req = 'heroes_to_upload_req.csv'
    outdict_req = calc_requested_heroes(hero_objs, request_dict)
    write_to_csv(outdict_req, filename_req)

    #abaddon = data['Abaddon']
    #abaddon['base_strength'] = 12.345

    #asdf = Hero(**abaddon)

    #for hero in hero_objs.keys():

    #    print("to_dict():\n{}".format(hero_objs[hero].to_dict()))
    #    print("to_dict():\n{}".format(hero_objs[hero].to_dict(title_case=True, rounded=True)))
    #    hero_objs[hero].level = 15
    #    print("to_dict():\n{}".format(hero_objs[hero].to_dict()))
    #    print("to_dict():\n{}".format(hero_objs[hero].to_dict(fields=Hero.OTHER_THING_FIELDS, title_case=True, rounded=True)))


if __name__ == '__main__':
    main()
