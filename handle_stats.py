import pandas as pd

def extract_hero_list(filename):
    with open(filename, 'r') as file_obj:
        df = pd.read_csv(file_obj)
        return list(df.hero.values)


def primary_attr_for_formulas(df):
    if (df['primary_attribute'] == 'strength'): 
        return df.strength
    if (df['primary_attribute'] == 'agility'): 
        return df.agility
    if (df['primary_attribute'] == 'intelligence'): 
        return df.intelligence
    else:
        raise exception

def calc_lvl_stats(filename, lvl=15):

    with open(filename, 'r') as file_obj:
        df = pd.read_csv(file_obj)

        # Changes to data happen
        df2 = pd.DataFrame({
            df.columns[0]: df.hero.values,
            'primary_attribute': df.primary_attribute.values,

            'strength': df.base_strength.values + \
                    (df.strength_growth.values * (lvl - 1)),
            'agility': df.base_agility.values + \
                    (df.agility_growth.values * (lvl - 1)),
            'intelligence': df.base_intelligence.values + \
                    (df.intelligence_growth.values * (lvl - 1))
            })
        df2['primary_attribute_count'] = df2.apply(primary_attr_for_formulas, axis=1)
        #print("after initial assignment: \n")
        #print(df2)

        #print(df2.agility.values)
        #print(df2['agility'].values)
        #new_df['Agility'] = df2.agility.values

        df2 = df2.assign(**{
            'total_attributes': df2.strength.values + df2.agility.values + \
                    df2.intelligence.values,
            'health': 200 + (df2.strength.values * 20),
            'health_regen': df.health_regen_0.values + \
                    (0.1 * df2.strength.values),
            'mana': df.mana_0.values + (12 * df2.intelligence.values),
            'mana_regen': df.mana_regen_0 + (0.05 * df2.intelligence.values),
            'armor': df.armor_0.values + ((1/6) * df2.agility.values),
            'attacks_per_second': (df.attack_speed.values + df2.agility.values * \
                    0.01) / df.base_attack_time.values,
            'damage_low': df.damage_low_0.values + \
                    df2.primary_attribute_count.values,
            'damage_high': df.damage_high_0.values + \
                    df2.primary_attribute_count.values
            })

        #print("after assign: \n")
        #print(df2)
        df2 = df2.round({
            'strength': 1,
            'agility': 1,
            'intelligence': 1,
            'total_attributes': 1,
            'health': 0,
            'health_regen': 1,
            'mana': 0,
            'mana_regen': 1,
            'armor': 2,
            'attacks_per_second': 2,
            'damage_low': 0,
            'damage_high': 0
            })
        df2.drop(['primary_attribute_count'], axis=1, inplace=True)
        
        #print("after round: \n")
        #print(df2)
        #df2.to_csv('out.csv')

        #df.drop([
        #    'health_0', 'health_15', 'health_25', 'health_30', 'health_regen_0',
        #    'health_regen_15', 'health_regen_25', 'health_regen_30', 'mana_0',
        #    'mana_15', 'mana_25', 'mana_30', 'mana_regen_0', 'mana_regen_15',
        #    'mana_regen_25', 'mana_regen_30', 'armor_0', 'armor_15', 'armor_25',
        #    'armor_30', 'attacks_per_second_0','attacks_per_second_15',
        #    'attacks_per_second_25', 'attacks_per_second_30', 'damage_low_0',
        #    'damage_low_15', 'damage_low_25', 'damage_low_30', 'damage_high_0',
        #    'damage_high_15', 'damage_high_25', 'damage_high_30'
        #], axis=1, inplace=True)

        # df for sheet displaying all hero stats
        out_df_all = df[[
            'hero',
            'primary_attribute',
            'base_strength',
            'strength_growth',
            'base_agility',
            'agility_growth',
            'base_intelligence',
            'intelligence_growth',
            'health_1',
            'health_regen_1',
            'mana_1',
            'mana_regen_1',
            'armor_1',
            'attacks_per_second_1',
            'damage_low_1',
            'damage_high_1',
            'magic_resistance',
            'movement_speed',
            'attack_speed',
            'turn_rate',
            'vision_range_day',
            'vision_range_night',
            'attack_type',
            'attack_range',
            'projectile_speed',
            'attack_animation_point',
            'attack_animation_backswing',
            'base_attack_time',
            'damage_block',
            'collision_size',
            'legs',
            'gib_type'
            ]].copy()
        print(out_df_all)
        
        #print(list(df.columns.values))
        out_df_all.rename({
            'hero': 'Hero',
            'primary_attribute': 'Primary Attribute',
            'base_strength': 'Base Strength',
            'strength_growth': 'Strength Growth',
            'base_agility': 'Base Agility',
            'agility_growth': 'Agility Growth',
            'base_intelligence': 'Base Intelligence',
            'intelligence_growth': 'Intelligence Growth',
            'health_1': 'Base Health',
            'health_regen_1': 'Base Health Regen',
            'mana_1': 'Base Mana',
            'mana_regen_1': 'Base Mana Regen',
            'armor_1': 'Base Armor',
            'attacks_per_second_1': 'Base Attacks/Second',
            'damage_low_1': 'Base Damage Low',
            'damage_high_1': 'Base Damage High',
            'magic_resistance': 'Magic Resistance',
            'movement_speed': 'Movement Speed',
            'attack_speed': 'Attack Speed',
            'turn_rate': 'Turn Rate',
            'vision_range_day': 'Vision Range Day',
            'vision_range_night': 'Vision Range Night',
            'attack_type': 'Attack Type',
            'attack_range': 'Attack Range',
            'projectile_speed': 'Projectile Speed',
            'attack_animation_point': 'Attack Animation Point',
            'attack_animation_backswing': 'Attack Animation Backswing',
            'base_attack_time': 'Base Attack Time',
            'damage_block': 'Damage Block',
            'collision_size': 'Collision Size',
            'legs': 'Legs',
            'gib_type': 'Gib Type'
            }, axis='columns', inplace=True)
        #print(list(df.columns.values)) 
        #print(df)

        print(list(out_df_all.columns.values))
        print(out_df_all)

        print(list(df2.columns.values))
        # df for sheet displaying requested hero stats
        print(out_df_req)
        
        #df2.to_csv(filename + '_to_upload.csv')
        #out_df_all.to_csv(filename + '_to_upload_sheet1.csv')
        #out_df_req.to_csv(filename + '_to_upload_sheet2.csv')


def main():
    # TODO - add argparse 

    filename='heroes.csv'

    # BEGIN temporary section
    #with open('hero_request.txt') as f:
    #    txt = f.read()
    #    req_hero = txt.split('\n')[0]
    #    print(req_hero)
    #    req_level = int(txt.split('\n')[1][1].strip())
    #    print(req_level)
    #    #global req_lvl = req_levels[0]
    #    #print(req_lvl)
    # END

    #extract_hero_list(filename)
    calc_lvl_stats(filename)


if __name__ == '__main__':
    main()
