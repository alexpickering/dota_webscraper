import pandas as pd
import numpy as np
import json


def extract_hero_list(filename):
    with open(filename, 'r') as file_obj:
        df = pd.read_csv(file_obj)
        return list(df.hero.values)


def calc_requested_heroes(filename):
    rows_list = []
    request_dict = {}
    with open('out_dict.json','r') as f:
        request_dict = json.load(f) 

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
                    'Armor': round(df.at[i, 'armor_0'] + ((1/6) * dict1['Agility']), 2),
                    'Attacks/Second': round((df.at[i, 'attack_speed'] + dict1['Agility'] * 0.01) / df.at[i, 'base_attack_time'], 2),
                    'Damage Low': round(df.at[i, 'damage_low_0'] + primary_attribute_count, 0),
                    'Damage High': round(df.at[i, 'damage_high_0'] + primary_attribute_count, 0)
                    })

                rows_list.append(dict1)
    outdf = pd.DataFrame(rows_list)
    print(outdf)
    outdf.to_csv('heroes_requested.csv',index=False)


def calc_all_heroes(filename):
    rows_list = []
    #with open('out_dict.json','r') as f:
    #    out_dict = json.load(f) 
    lvl = 15

    with open(filename, 'r') as file_obj:
        df = pd.read_csv(file_obj)
        hero_list = df.hero.values

        # iterates through keys
        for hero in hero_list:
            i = df.index[df['hero'] == hero].tolist()[0]
            #print(json.dumps(out_dict))
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
                'Armor': round(df.at[i, 'armor_0'] + ((1/6) * dict1['Agility']), 2),
                'Attacks/Second': round((df.at[i, 'attack_speed'] + dict1['Agility'] * 0.01) / df.at[i, 'base_attack_time'], 2),
                'Damage Low': round(df.at[i, 'damage_low_0'] + primary_attribute_count, 0),
                'Damage High': round(df.at[i, 'damage_high_0'] + primary_attribute_count, 0)
                })

            rows_list.append(dict1)
    outdf = pd.DataFrame(rows_list)
    print(outdf)
    outdf.to_csv('heroes_all.csv',index=False)


def main():
    filename = 'heroes.csv'
    calc_requested_heroes(filename)
    calc_all_heroes(filename)


if __name__ == '__main__':
    main()
