#!/usr/bin/env python3
import sys
from argparse import ArgumentParser
from gooey import Gooey


def with_gui():
    pass

@Gooey
def main():

    if len(sys.argv) == 1:
        with_gui()

    print(ArgumentParser)

    parser = ArgumentParser()
    parser.add_argument("--hero", type=str, action='append', nargs='+')
    args = parser.parse_args()

    print(args.hero)

    heroes = {}

    for hero in args.hero:
        levels = []

        for chunk in hero[1].split(','):
            if '-' in chunk:
                start, end = chunk.split('-')
                start = int(start.strip())
                end   = int(end.strip())
                levels += [lvl for lvl in range(start, end+1)]

            else:
                levels.append(int(chunk.strip()))

        heroes[0] = levels
        #print(hero[0])
        #print(levels)
    
    print(heroes)


if __name__ == '__main__':
    main()
