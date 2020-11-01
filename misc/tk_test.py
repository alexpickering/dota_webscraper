import tkinter as tk 
from ttkwidgets.autocomplete import AutocompleteEntryListbox as Autobox


def hit_return(key_event):
    print('You hit return')
    return True


def main():
    window = tk.Tk() 

    hero_list = ['Alchemist',  'Axe', 'Lone Druid', 'Enigma', 'Abaddon']
    tk.Label(window, text="Select a Hero: ").pack()
    req_heroes = Autobox(window,completevalues=hero_list, allow_other_values=False)
    req_heroes.pack()
    window.bind('<Return>', hit_return)



    window.mainloop() 


if __name__ == '__main__':
    main()
