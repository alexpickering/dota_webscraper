import pandas as pd

def primary_attr_for_formulas(df):
    if (df['primary_attribute'] == 'strength'): 
        return df.strength
    if (df['primary_attribute'] == 'agility'): 
        return df.agility
    if (df['primary_attribute'] == 'intelligence'): 
        return df.intelligence
    else:
        raise exception


with open('heroes.csv', 'r') as file_obj:
    data = pd.read_csv(file_obj)

    # Changes to data happen
    lvl = 15 
    df2 = pd.DataFrame({
        data.columns[0]: data.hero.values,
        'primary_attribute': data.primary_attribute.values,

	'strength': data.base_strength.values + \
                (data.strength_growth.values * (lvl - 1)),
        'agility': data.base_agility.values + \
                (data.agility_growth.values * (lvl - 1)),
	'intelligence': data.base_intelligence.values + \
                (data.intelligence_growth.values * (lvl - 1))
        })
    df2['primary_attribute_count'] = df2.apply(primary_attr_for_formulas, axis=1)
    #print("after initial assignment: \n")
    #print(df2)


    df2 = df2.assign(**{
        'total_attributes': df2.strength.values + df2.agility.values + \
                df2.intelligence.values,
        'health': 200 + (df2.strength.values * 20),
        'health_regen': data.health_regen_0.values + \
                (0.1 * df2.strength.values),
        'mana': data.mana_0.values + (12 * df2.intelligence.values),
        'mana_regen': data.mana_regen_0 + (0.05 * df2.intelligence.values),
        'armor': data.armor_0.values + ((1/6) * df2.agility.values),
        'attacks_per_second': (data.attack_speed.values + df2.agility.values * \
                0.01) / data.base_attack_time.values,
        'damage_low': data.damage_low_0.values + \
                df2.primary_attribute_count.values,
        'damage_high': data.damage_high_0.values + \
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
    df2.to_csv('out.csv')

    data.drop([
        'health_0', 'health_15', 'health_25', 'health_30', 'health_regen_0',
        'health_regen_15', 'health_regen_25', 'health_regen_30', 'mana_0',
        'mana_15', 'mana_25', 'mana_30', 'mana_regen_0', 'mana_regen_15',
        'mana_regen_25', 'mana_regen_30', 'armor_0', 'armor_15', 'armor_25',
        'armor_30', 'attacks_per_second_0','attacks_per_second_15',
        'attacks_per_second_25', 'attacks_per_second_30', 'damage_low_0',
        'damage_low_15', 'damage_low_25', 'damage_low_30', 'damage_high_0',
        'damage_high_15', 'damage_high_25', 'damage_high_30'
    ], axis=1, inplace=True)

    #for hero in data:
    #print(data)
    #print(list(data.columns.values))
    data.rename({
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
    #print(list(data.columns.values)) 
    #print(data)


    #df2.to_csv('out.csv')
