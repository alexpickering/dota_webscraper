#!/bin/bash

rm test.db
sqlite3 test.db < setup.sql
sqlite3 test.db 'select name, base_strength, strength_growth, damage_low_1, damage_high_1, movement_speed from hero;'

# TODO: write a query that returns a list of the heroes in ORDER of DESCending movement_speed
sqlite3 test.db 'select name, movement_speed from hero order by movement_speed desc;'

# TODO: write a query that returns the fastest hero (movement_speed)
sqlite3 test.db 'select name, movement_speed from hero order by movement_speed desc limit 1;'

# TODO: write a query that returns heroes who move faster than 305, ordered from fastest to slowest
sqlite3 test.db 'select name, movement_speed from hero where movement_speed > 305 order by movement_speed desc;'

# TODO: write a query that returns the hero's name and their damage variance (max_damage - min_damage)
# https://www.w3resource.com/sql/arithmetic-operators/sql-arithmetic-operators.php
sqlite3 test.db 'select name, (damage_high_1 - damage_low_1) as damage_variance from hero;'
