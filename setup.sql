CREATE TABLE hero (
    name STRING PRIMARY KEY,
    base_strength INTEGER,
    strength_growth FLOAT,
    base_agility INTEGER,
    agility_growth FLOAT,
    base_intelligence INTEGER,
    intelligence_growth FLOAT,
    health_0 INTEGER,
    health_1 INTEGER,
    health_15 INTEGER,
    health_25 INTEGER,
    health_30 INTEGER,
    health_regen_0 FLOAT,
    health_regen_1 FLOAT,
    health_regen_15 FLOAT,
    health_regen_25 FLOAT,
    health_regen_30 FLOAT,
    mana_0 INTEGER,
    mana_1 INTEGER,
    mana_15 INTEGER,
    mana_25 INTEGER,
    mana_30 INTEGER,
    mana_regen_0 FLOAT,
    mana_regen_1 FLOAT,
    mana_regen_15 FLOAT,
    mana_regen_25 FLOAT,
    mana_regen_30 FLOAT,
    attacks_per_second_0 FLOAT,
    attacks_per_second_1 FLOAT,
    attacks_per_second_15 FLOAT,
    attacks_per_second_25 FLOAT,
    attacks_per_second_30 FLOAT,
    damage_low_0 INTEGER,
    damage_high_0 INTEGER,
    damage_low_1 INTEGER,
    damage_high_1 INTEGER,
    damage_low_15 INTEGER,
    damage_high_15 INTEGER,
    damage_low_25 INTEGER,
    damage_high_25 INTEGER,
    damage_low_30 INTEGER,
    damage_high_30 INTEGER,
    magic_resistance decimal(3,2),
    movement_speed INTEGER,
    attack_speed INTEGER
);

INSERT INTO hero (name, base_strength) VALUES ("Abbadon", 20);

INSERT INTO hero (
    name, 
    base_strength, 
    strength_growth, 
    damage_low_1, 
    damage_high_1, 
    movement_speed
    ) VALUES(
    "Lone Druid",



);

INSERT INTO hero (
    name, 
    base_strength, 
    strength_growth, 
    damage_low_1, 
    damage_high_1, 
    movement_speed
    ) VALUES(
    "Lone Druid",



);

INSERT INTO hero (
    name, 
    base_strength, 
    strength_growth, 
    damage_low_1, 
    damage_high_1, 
    movement_speed
    ) VALUES(
    "Lone Druid",



);
