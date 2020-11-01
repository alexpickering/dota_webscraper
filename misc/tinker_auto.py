#!/usr/bin/env python3

import tkinter as tk

def on_keypress(event):

    # get text from entry
    if event.keysym == 'BackSpace':
        # remove last char
        value = event.widget.get()[:-1]
    elif (event.state & 4): # and (event.keysym in ('a', 'c', 'x', 'e')):
        value = event.widget.get()
    else:
        # add new char at the end        
        value = event.widget.get() + event.char

    value = value.strip().lower()

    # get data from test_list
    if value == '':
        data = test_list
    else:
        data = []
        for item in test_list:
            if value in item.lower():
                data.append(item)                

    # update data in listbox
    listbox_update(data)


def listbox_update(data):
    # delete previous data
    listbox.delete(0, 'end')

    # sorting data 
    data = sorted(data, key=str.lower)

    # put new data
    for item in data:
        listbox.insert('end', item)


def on_select(event):
    # display element selected on list
    print('(event) previous:', event.widget.get('active'))
    print('(event)  current:', event.widget.get(event.widget.curselection()))
    print('---')


# --- main ---

test_list = ('apple', 'banana', 'Cranberry', 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' )

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()
entry.bind('<KeyPress>', on_keypress)

listbox = tk.Listbox(root)
listbox.pack()
#listbox.bind('<Double-Button-1>', on_select)
listbox.bind('<<ListboxSelect>>', on_select)
listbox_update(test_list)

root.mainloop()
