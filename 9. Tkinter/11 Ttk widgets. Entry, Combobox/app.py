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

button = ttk.Button(frame, text='Okay')
button.grid()


measureSystem = StringVar()
check = ttk.Checkbutton(frame, text='Use Metric',
                        variable=measureSystem,
                        onvalue='metric', offvalue='imperial')
check.grid()

phone = StringVar()
home = ttk.Radiobutton(frame, text='Home', variable=phone, value='home')
office = ttk.Radiobutton(frame, text='Office', variable=phone, value='office')
cell = ttk.Radiobutton(frame, text='Mobile', variable=phone, value='cell')

home.grid()
office.grid()
cell.grid()

username = StringVar()
name = ttk.Entry(frame, textvariable=username)
name.grid()

countryvar = StringVar()
country = ttk.Combobox(frame, textvariable=countryvar)
country['values'] = ('USA', 'Canada', 'Australia')
country.grid()

root.mainloop()
