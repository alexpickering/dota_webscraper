#!/usr/bin/env python3
import sys
from argparse import ArgumentParser
from gooey import Gooey, GooeyParser


def with_gui():
    pass

@Gooey(advanced=True)
def main():

    if len(sys.argv) == 1:
        with_gui()

    parser = GooeyParser(description="Input Heroes and Levels for Level-Dependent Stats")
    parser.add_argument('--hero', metavar='Hero(es)', help='Enter Heroes Below', type=str, action='append', nargs='+')
    #parser.add_argument('--level', type=int, metavar='Level(s)', help='Select Level(s)', widget='Listbox', choices=range(1,31), nargs='+')
    #parser.add_argument("--level", type=str, action='append', nargs='+')
    args = parser.parse_args()

    print(args.hero)
    #print(args.level)

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
        print(hero[0])
        print(levels)
    
    print(heroes)
    with open('hero_request.txt', 'w') as f:
        f.write(str(hero[0]) + '\n' + str(levels) + '\n')
    

if __name__ == '__main__':
    main()
