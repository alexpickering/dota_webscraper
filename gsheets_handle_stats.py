import csv
import json
import pandas as pd


def get_request_dict(filename):
    request_dict = {}
    with open(filename, 'r') as f:
        request_dict = json.loads(f.read())
    return request_dict

def calc_all_heroes(datafile_name, all_lvl, outfile_name):
    rows = []

    with open(datafile_name, 'r') as file_obj:
        df = pd.read_csv(file_obj)

        # track index of requested heroes
        # gsheets is 1-indexed, 1 is Level:, all_lvl, 2 is header rows, heroes start at 3
        new_index = str(3)

        headers = {'Hero': '$A', 'Primary': '$B', 'Strength': '$C', 'Agility': '$D','Intelligence': '$E', 'Attribute Total': '$F'}

        hero_list = df.hero.values

        for hero in hero_list:
            i = df.index[df['hero'] == hero].tolist()[0]

            dict1 = {}

            # store frequently used variables for clarity
            primary, = str(df.at[i,'primary_attribute']),
            base_strength = str(df.at[i,'base_strength'])
            strength_growth = str(df.at[i,'strength_growth'])
            base_agility = str(df.at[i,'base_agility'])
            agility_growth = str(df.at[i,'agility_growth'])
            base_intelligence = str(df.at[i,'base_intelligence'])
            intelligence_growth = str(df.at[i,'intelligence_growth'])
            base_health_regen = str(df.at[i,'health_regen_0'])
            base_mana = str(df.at[i,'mana_0'])
            base_mana_regen = str(df.at[i,'mana_regen_0'])
            base_armor = str(df.at[i,'armor_0'])
            attack_speed = str(df.at[i,'attack_speed'])
            base_attack_time = str(df.at[i,'base_attack_time'])
            base_damage_low = str(df.at[i,'damage_low_0'])
            base_damage_high = str(df.at[i,'damage_high_0'])
            
            # cell reference in A1 (ex. $D3)
            primary_cell = ''.join([headers[primary.title()],new_index])
            strength_cell = ''.join([headers['Strength'],new_index])
            agility_cell = ''.join([headers['Agility'],new_index])
            intelligence_cell = ''.join([headers['Intelligence'],new_index])
            all_lvl_cell = '$B$1'

            # cell values defined
            strength_cell_val = ''.join(['=',base_strength,'+',strength_growth,'*(',all_lvl_cell,'-1)'])
            agility_cell_val = ''.join(['=',base_agility,'+',agility_growth,'*(',all_lvl_cell,'-1)'])
            intelligence_cell_val = ''.join(['=',base_intelligence,'+',intelligence_growth,'*(',all_lvl_cell,'-1)'])
            total_attr_val = ''.join(['=',strength_cell,'+',agility_cell,'+',intelligence_cell])
            health = ''.join(['=200+(rounddown(',strength_cell,')*20)'])
            health_regen = ''.join(['=',base_health_regen,'+(0.1*',strength_cell,')'])
            mana = ''.join(['=',base_mana,'+(12*rounddown(',intelligence_cell,'))'])
            mana_regen = ''.join(['=',base_mana_regen,'+(0.05*',intelligence_cell,')'])
            armor = ''.join(['=round(',base_armor,'+((1/6)*',agility_cell,'),2)'])
            attacks_per_second = ''.join(['=round(((',attack_speed,'+',agility_cell,')*0.01)/',base_attack_time,',2)'])
            damage_low = ''.join(['=',base_damage_low,'+rounddown(',primary_cell,')'])
            damage_high = ''.join(['=',base_damage_high,'+rounddown(',primary_cell,')'])


            # assign values to temporary dictionary
            dict1.update({
                    'Hero': hero,
                    'Primary': primary,
                    'Strength': strength_cell_val,
                    'Agility': agility_cell_val,
                    'Intelligence': intelligence_cell_val,
                    'Total Attributes': total_attr_val,
                    'Health': health,
                    'Health Regen': health_regen,
                    'Mana': mana,
                    'Mana Regen': mana_regen,
                    'Armor': armor,
                    'Attacks/Second': attacks_per_second,
                    'Damage Low': damage_low,
                    'Damage High': damage_high
            })

            rows.append(dict1)
            new_index = str(int(new_index)+1)

    outdf = pd.DataFrame(rows)
    outdf.to_csv(outfile_name,index=False)

    with open(outfile_name, 'r') as file_obj:
        finaldf = pd.read_csv(file_obj,header=None)
        
        end_headers = ['Level:', all_lvl,] + [''] * 12
        finaldf.columns = end_headers
        finaldf.to_csv(outfile_name,index=False)


def calc_requested_heroes(datafile_name, request_dict,outfile_name):
    rows = []

    with open(datafile_name, 'r') as file_obj:
        df = pd.read_csv(file_obj)

        # Add Level column with default value 1
        df.insert(1, 'Level', 1)

        # track index of requested heroes
        new_index = str(2)

        headers = {'Hero':'$A', 'Level': '$B', 'Primary': '$C', 'Strength': '$D','Agility':'$E','Intelligence':'$F', 'Attribute Total': '$G'}

        for hero, lvls in request_dict.items():
            i = df.index[df['hero'] == hero].tolist()[0]
            for lvl in lvls:
                dict1 = {}
                # store frequently used variables for clarity
                primary, = str(df.at[i,'primary_attribute']),
                base_strength = str(df.at[i,'base_strength'])
                strength_growth = str(df.at[i,'strength_growth'])
                base_agility = str(df.at[i,'base_agility'])
                agility_growth = str(df.at[i,'agility_growth'])
                base_intelligence = str(df.at[i,'base_intelligence'])
                intelligence_growth = str(df.at[i,'intelligence_growth'])
                base_health_regen = str(df.at[i,'health_regen_0'])
                base_mana = str(df.at[i,'mana_0'])
                base_mana_regen = str(df.at[i,'mana_regen_0'])
                base_armor = str(df.at[i,'armor_0'])
                attack_speed = str(df.at[i,'attack_speed'])
                base_attack_time = str(df.at[i,'base_attack_time'])
                base_damage_low = str(df.at[i,'damage_low_0'])
                base_damage_high = str(df.at[i,'damage_high_0'])
                
                # cell reference in A1 (ex. $D3)
                primary_cell = ''.join([headers[primary.title()],new_index])
                strength_cell = ''.join([headers['Strength'],new_index])
                agility_cell = ''.join([headers['Agility'],new_index])
                intelligence_cell = ''.join([headers['Intelligence'],new_index])

                # cell values defined
                strength_cell_val = ''.join(['=',base_strength,'+',strength_growth,'*(',headers['Level'],new_index,'-1)'])
                agility_cell_val = ''.join(['=',base_agility,'+',agility_growth,'*(',headers['Level'],new_index,'-1)'])
                intelligence_cell_val = ''.join(['=',base_intelligence,'+',intelligence_growth,'*(',headers['Level'],new_index,'-1)'])
                total_attr_val = ''.join(['=',strength_cell,'+',agility_cell,'+',intelligence_cell])
                health = ''.join(['=200+(rounddown(',strength_cell,')*20)'])
                health_regen = ''.join(['=',base_health_regen,'+(0.1*',strength_cell,')'])
                mana = ''.join(['=',base_mana,'+(12*rounddown(',intelligence_cell,'))'])
                mana_regen = ''.join(['=',base_mana_regen,'+(0.05*',intelligence_cell,')'])
                armor = ''.join(['=',base_armor,'+((1/6)*',agility_cell,')'])
                attacks_per_second = ''.join(['=((',attack_speed,'+',agility_cell,')*0.01)/',base_attack_time])
                damage_low = ''.join(['=',base_damage_low,'+rounddown(',primary_cell,')'])
                damage_high = ''.join(['=',base_damage_high,'+rounddown(',primary_cell,')'])


                # assign values to temporary dictionary
                dict1.update({
                        'Hero': ''.join(['="',hero,'_"&',headers['Level'],new_index]),
                        'Level': lvl,
                        'Primary': primary,
                        'Strength': strength_cell_val,
                        'Agility': agility_cell_val,
                        'Intelligence': intelligence_cell_val,
                        'Total Attributes': total_attr_val,
                        'Health': health,
                        'Health Regen': health_regen,
                        'Mana': mana,
                        'Mana Regen': mana_regen,
                        'Armor': armor,
                        'Attacks/Second': attacks_per_second,
                        'Damage Low': damage_low,
                        'Damage High': damage_high
                })

            rows.append(dict1)
            new_index = str(int(new_index)+1)

    outdf = pd.DataFrame(rows)
    outdf.to_csv(outfile_name,index=False)
    #outdf.to_csv(outfile_name,index=False)


def calc_requests(datafile_name, request_dict):
    all_lvl = request_dict.pop('All Heroes', 1)

    filename_all = 'heroes_to_upload_all.csv'
    outdict_all = calc_all_heroes(datafile_name, all_lvl, filename_all)

    filename_req = 'heroes_to_upload_req.csv'
    outdict_req = calc_requested_heroes(datafile_name, request_dict, filename_req)

    return (filename_all, filename_req)


def main():
    datafile_name = 'heroes.csv'
    request_dict_filename = 'request.json'

    request_dict = get_request_dict(request_dict_filename)
    all_lvl = request_dict.pop('All Heroes', 1)

    filename_all = 'heroes_to_upload_all.csv'
    outdict_all = calc_all_heroes(datafile_name, all_lvl, filename_all)

    filename_req = 'heroes_to_upload_req.csv'
    outdict_req = calc_requested_heroes(datafile_name, request_dict, filename_req)



if __name__ == '__main__':
    main()
