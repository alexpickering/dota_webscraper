#!/usr/bin/env python3
import argparse
import pandas as pd

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_csv', type=str, default='heroes.csv')
    parser.add_argument('output_db', type=str, default='heroes.db')
    args = parser.parse_args()

    hero_data = pd.read_csv(args.input_csv)
    hero_data.to_sql('hero', f'sqlite:///{args.output_db}', if_exists='append', index=False)


if __name__ == '__main__':
    main()
