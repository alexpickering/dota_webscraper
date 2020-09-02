#!/usr/bin/env python3
import argparse
import csv
import sqlite3

setup_sql = 'setup.sql'
csv_file = 'heroes.csv'
db_name = 'heroes.db'

con = sqlite3.connect(db_name)
cur = con.cursor()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--todo")
    args = parser.parse_args()

    # Create the db table 'hero' from our SQL definition
    with open(setup_sql) as f:
        setup = f.read()
    cur.execute(setup)

    # Populate the db with our csv data
    with open(csv_file) as f:
        columns_line = f.readline().strip()

        hero_rows = []
        while True:
            # Read the next line. If it's not there, then we're done.
            line = f.readline()
            if not line:
                break

            # This gets: ["Abbadon", "24", "123", ...]
            hero_row = line.strip().split(',')
            # Actually we want a tuple: ("Abbadon", "24", "123", ...)
            hero_row = tuple(hero_row)

            # Add this hero row data to the full collection
            hero_rows.append(hero_row)

            # Limit while we're still testing
            #if len(hero_rows) > 3:
            #    break



    # Unfortunately we need a string like: "?,?,?,?,?,?"
    # Each ? represents a value in execute() and executemany()
    questions = "?,"*len(hero_rows[0])
    questions = questions[:-1]

    # Option 1: Insert as a string...
    #cur.execute("INSERT INTO hero ({}) VALUES ({});".format(columns_line, first_row))
    # Option 2: Insert one row at a time (tuple form)
    #cur.execute("INSERT INTO hero ({}) VALUES ({});".format(columns_line, questions), hero_rows[0])
    # Option 3: Insert all rows at once (pass as a list of tuples)
    cur.executemany("INSERT INTO hero ({}) VALUES ({});".format(columns_line, questions), hero_rows)


    con.commit()
    con.close()


if __name__ == '__main__':
    main()
