from tkinter import *
from tkinter import ttk
root = Tk()

frame = ttk.Frame(root, width=200, height=200)
frame.grid()
frame['borderwidth'] = 10
frame['relief'] = 'raised'

root.mainloop()