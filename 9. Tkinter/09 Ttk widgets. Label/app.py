from tkinter import *
from tkinter import ttk
root = Tk()

frame = ttk.Frame(root, width=200, height=200, padding=5)
frame.grid()
frame['borderwidth'] = 10
frame['relief'] = 'raised'

label = ttk.Label(frame, text='Full name:')
label.grid()

resultsContents = StringVar()
label['textvariable'] = resultsContents
resultsContents.set('New value to display')

root.mainloop()