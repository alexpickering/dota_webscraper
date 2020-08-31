#!/bin/bash

rm test.db
sqlite3 test.db < setup.sql
sqlite3 test.db 'select name, base_strength, strength_growth, damage_low_1, damage_high_1, movement_speed from hero;'

# TODO: write a query that returns a list of the heroes in ORDER of DESCending movement_speed


# TODO: write a query that returns the fastest hero (movement_speed)


# TODO: write a query that returns heroes who move faster than 305, ordered from fastest to slowest


# TODO: write a query that returns the hero's name and their damage variance (max_damage - min_damage)
# https://www.w3resource.com/sql/arithmetic-operators/sql-arithmetic-operators.php
