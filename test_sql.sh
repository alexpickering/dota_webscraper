#!/bin/bash

rm test.db
sqlite3 test.db < setup.sql
sqlite3 test.db 'select name, base_strength, strength_growth, damage_low_1, damage_high_1, movement_speed from hero;'
