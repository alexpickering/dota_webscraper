import pandas as pd
import numpy as np
import json
import csv
import copy
from hero import Hero


def using_csv(filename):
    with open(filename, 'r') as f:
        raw = csv.DictReader(f)

        data = {}
        for elt in raw:
            data[elt['hero']] = elt

    return data


def calc_from_dict(filename, full_data, request_dict):
    del request_dict['All Heroes']

    row_list = []
    with open(filename, 'r') as file_obj:
        df = pd.read_csv(file_obj)

    print(df.keys())

    # Try to cast values as other data types (they're all loaded as strings)
    for col in df.keys():
        try:
            df[col] = df[col].astype(int)
        except ValueError as e:
            try:
                df[col] = df[col].astype(float)
            except ValueError as e:
                pass

    records = {}
    for elt in df.to_dict('records'):
        records[elt['hero']] = elt

    for hero, lvls in request_dict.items():
        for lvl in lvls:
            hero_orig = records[hero]
            
            row = {
                'Hero': "{}_{}".format(hero, lvl),
                'Primary Attribute': hero_orig['primary_attribute'],
                'Strength': hero_orig['base_strength'] + (hero_orig['strength_growth'] * (lvl-1))

                }
            print(row)


def extract_hero_list(filename):
    with open(filename, 'r') as file_obj:
        df = pd.read_csv(file_obj)
        return list(df.hero.values)


def calc_requested_heroes(filename, request_dict):
    del request_dict['All Heroes']
    rows_list = []
    #request_dict = {}
    #with open('out_dict.json','r') as f:
    #    request_dict = json.load(f) 

    with open(filename, 'r') as file_obj:
        df = pd.read_csv(file_obj)

        # iterates through keys
        for hero, lvls in request_dict.items():
            i = df.index[df['hero'] == hero].tolist()[0]
            #print(json.dumps(request_dict))
            for lvl in lvls:
                dict1 = {}
                dict1.update({
                    'Hero': hero + '_' + str(lvl),
                    'Primary Attribute': df.at[i, 'primary_attribute'],
                    'Strength': round(df.at[i, 'base_strength'] + (df.at[i, 'strength_growth'] * (lvl - 1)), 1),
                    'Agility': round(df.at[i, 'base_agility'] + (df.at[i, 'agility_growth'] * (lvl - 1)), 1),
                    'Intelligence': round(df.at[i, 'base_intelligence'] + (df.at[i, 'intelligence_growth'] * (lvl - 1)), 1),
                    })
                primary_attribute_count = dict1[dict1['Primary Attribute'].title()]

                dict1.update({
                    'Total Attributes': round(dict1['Strength'] + dict1['Agility'] + dict1['Intelligence'], 1),
                    'Health': round(200 + (dict1['Strength'] * 20), 0),
                    'Health Regen': round(df.at[i, 'health_regen_0'] + (0.1 * dict1['Strength']), 1),
                    'Mana': round(df.at[i, 'mana_0'] + (12 * dict1['Intelligence']), 0),
                    'Mana Regen': round(df.at[i, 'mana_regen_0'] + (0.05 * dict1['Intelligence']), 1),
                    'Armor': round(df.at[i, 'armor_0'] + ((1.0/6) * dict1['Agility']), 2),
                    'Attacks/Second': round((df.at[i, 'attack_speed'] + dict1['Agility'] * 0.01) / df.at[i, 'base_attack_time'], 2),
                    'Damage Low': round(df.at[i, 'damage_low_0'] + primary_attribute_count, 0),
                    'Damage High': round(df.at[i, 'damage_high_0'] + primary_attribute_count, 0)
                    })

                rows_list.append(dict1)
    outdf = pd.DataFrame(rows_list)
    print(outdf)
    outdf.to_csv('heroes_requested.csv',index=False)


def calc_all_heroes(filename, request_dict):
    rows_list = []
    #with open('out_dict.json','r') as f:
    #    out_dict = json.load(f) 
    lvl = request_dict['All Heroes']
    del request_dict['All Heroes']

    with open(filename, 'r') as file_obj:
        df = pd.read_csv(file_obj)
        hero_list = df.hero.values
        #df.astype('int64').dtypes

        # iterates through keys
        for hero in hero_list:
            i = df.index[df['hero'] == hero].tolist()[0]
            #print(json.dumps(out_dict))
            dict1 = {}
            print(df.at[i, 'base_strength'])
            print(df.at[i, 'strength_growth'])
            print("base_strength int?: {}\nstrength_growth int?: {}\n".format(type(df.at[i, 'base_strength']), type(df.at[i, 'strength_growth'])))
            dict1.update({
                'Hero': hero + '_' + str(lvl),
                'Primary Attribute': df.at[i, 'primary_attribute'],
                'Strength': round(int(df.at[i, 'base_strength'] + (df.at[i, 'strength_growth'] * (lvl - 1))), 1),
                'Agility': round(df.at[i, 'base_agility'] + (df.at[i, 'agility_growth'] * (lvl - 1)), 1),
                'Intelligence': round(df.at[i, 'base_intelligence'] + (df.at[i, 'intelligence_growth'] * (lvl - 1)), 1),
                })
            primary_attribute_count = dict1[dict1['Primary Attribute'].title()]

            dict1.update({
                'Total Attributes': round(dict1['Strength'] + dict1['Agility'] + dict1['Intelligence'], 1),
                'Health': round(200 + (dict1['Strength'] * 20), 0),
                'Health Regen': round(df.at[i, 'health_regen_0'] + (0.1 * dict1['Strength']), 1),
                'Mana': round(df.at[i, 'mana_0'] + (12 * dict1['Intelligence']), 0),
                'Mana Regen': round(df.at[i, 'mana_regen_0'] + (0.05 * dict1['Intelligence']), 1),
                'Armor': round(df.at[i, 'armor_0'] + ((1/6) * dict1['Agility']), 2),
                'Attacks/Second': round((df.at[i, 'attack_speed'] + dict1['Agility'] * 0.01) / df.at[i, 'base_attack_time'], 2),
                'Damage Low': round(df.at[i, 'damage_low_0'] + primary_attribute_count, 0),
                'Damage High': round(df.at[i, 'damage_high_0'] + primary_attribute_count, 0)
                })

            rows_list.append(dict1)
    outdf = pd.DataFrame(rows_list)
    print(outdf)
    outdf.to_csv('heroes_all.csv',index=False)

def calc_handler(filename, request_dict):
    if 'All Heroes' in request_dict and len(request_dict.keys()) > 1:
        return list(calc_all_heroes(filename, request_dict), calc_requested_heroes(filename, request_dict))
    elif 'All Heroes' in request_dict:
        return list(calc_all_heroes(filename, request_dict))
    elif len(request_dict.keys()) > 0:
        return list(calc_requested_heroes(filename, request_dict))
    else:
        raise Exception("request_dict is empty")



def main():
    test_filename = 'heroes.csv'
    test_request_dict = {'All Heroes': 15, 'Abaddon': [2,4,11]}
    
    #calc_handler(test_filename, test_request_dict)
    #calc_all_heroes(test_filename, test_request_dict)
    data = using_csv(test_filename)
    #print(data)
    abaddon = data['Abaddon']
    abaddon['base_strength'] = 12.345

    asdf = Hero(**abaddon)
    
    
    
    #class_heroes = [Hero(**data[elt]) for elt in data.keys()]

    print("to_dict():\n{}".format(asdf.to_dict()))
    print("to_dict():\n{}".format(asdf.to_dict(title_case=True, rounded=True)))
    asdf.level = 10
    print("to_dict():\n{}".format(asdf.to_dict()))
    print("to_dict():\n{}".format(asdf.to_dict(title_case=True, rounded=True)))
    #print("to_dict():\n{}".format(asdf.to_dict(rounded=False)))


    #asdf.level = 5
    #print(asdf.rounded_dict())


if __name__ == '__main__':
    main()
