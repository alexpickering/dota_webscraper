from argparse import ArgumentParser
from gooey import Gooey, GooeyParser
from handle_stats import extract_hero_list
import re


@Gooey
def parse_input():
    parser = ArgumentParser()
    parser.add_argument('hero', action='extend', type=str,  nargs='+', metavar='Hero and Level')
    args = parser.parse_args()
    heroes = args.hero
    print("parser output: ")
    print(heroes)
    raw_list = []

    print("regex split: ")
    print(re.split(',| ', ' '.join(heroes)))

    for elt in re.split(',| ', ' '.join(heroes)):
        if '-' in elt:
            start, end = elt.split('-')
            start = int(start.strip())
            end   = int(end.strip())
            raw_list += [lvl for lvl in range(start, end+1)]
        else:
            raw_list.append(elt)

    raw_list = list(filter(None, raw_list))    

    print("raw_list: ")
    print(raw_list)

    hero_list = extract_hero_list('heroes.csv')
    # num_list strings: [ '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
    num_list = list(range(1,31))
    rough_list= []

    for hero in raw_list:
        if isinstance(hero, int):
            rough_list.append(hero)
        else:
            rough_list += (listhero for listhero in hero_list if hero.lower() in listhero.lower())
            rough_list += (n for n in num_list if hero.isnumeric() and int(hero) == n)

    print("rough_list:")
    print(rough_list)

    deduped_list = []

    for elt in rough_list:
        if isinstance(elt, int) or elt not in deduped_list:
            deduped_list.append(elt)

    print("deduped_list:")
    print(deduped_list)


    out_dict = {}

    i = 0
    val_list = []
    list_length = len(deduped_list)
    while i < list_length:
        if i < list_length-1 and isinstance(deduped_list[i+1], int):
            hero_name = deduped_list[i]
            val_list.clear()
            while i < list_length-1 and isinstance(deduped_list[i+1], int):
                val_list.append(deduped_list[i+1])
                i = i + 1
                #print(val_list)
                #print("first while " + str(i))
            out_dict[hero_name] = sorted(val_list.copy())
            i = i + 1
            #print(out_dict)
            #print("second, after out_dict " + str(i))
        else:
            hero_name = deduped_list[i]
            out_dict[hero_name] = [1]
            i = i + 1
            #print("third, in else " + str(i))


    print(out_dict)
    return out_dict


def main():
    return parse_input()

if __name__ == '__main__':
    main()
