import tkinter as tk
from ttkwidgets.autocomplete import AutocompleteEntryListbox

window = tk.Tk()
tk.Label(window, text="Entry + Listbox with autocompletion for the Tk instance's methods:").pack()
entry = AutocompleteEntryListbox(window, width=20, completevalues=dir(window))
entry.pack()
window.mainloop()
