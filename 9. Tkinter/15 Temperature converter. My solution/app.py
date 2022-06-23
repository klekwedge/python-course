import tkinter as tk
from tkinter import ttk


def calculate():
    try:
        pass
        value = float(celsius_value.get())
        fahrenheit_value.set(int((value * 9/5) + 32))
    except ValueError:
        pass


root = tk.Tk()
root.title('Temperature converter')

root.columnconfigure(0, weight=1)


input_frame = ttk.Frame(root, padding=(10, 5, 10, 0))
input_frame.grid(row=0, column=0, sticky='EW')
input_frame.columnconfigure(0, weight=1)

celsius_label = ttk.Label(input_frame, text='Celsius: ')
celsius_label.grid(padx=(5, 10))

celsius_value = tk.StringVar()
celsius_entry = ttk.Entry(input_frame, width=20, textvariable=celsius_value)
celsius_entry.grid(row=0, column=1, padx=(5, 10))
celsius_entry.focus()

fahrenheit_label = ttk.Label(input_frame, text='Fahrenheit: ')
fahrenheit_label.grid(padx=(5, 10), row=1, column=0)

fahrenheit_value = tk.StringVar(value='Temp in Fahrenheit')
fahrenheit_calc = ttk.Label(input_frame, textvariable=fahrenheit_value)
fahrenheit_calc.grid(padx=(5, 10), row=1, column=1, sticky='W')

buttons_frame = ttk.Frame(root, padding=(10, 5))
buttons_frame.grid(row=1, column=0, sticky='EW')
buttons_frame.columnconfigure(0, weight=1)

convert_button = ttk.Button(buttons_frame, text='Convert', command=calculate)
convert_button.grid(row=0, column=0, sticky='EW')

root.mainloop()
