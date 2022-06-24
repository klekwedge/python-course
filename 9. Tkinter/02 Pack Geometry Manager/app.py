from tkinter import *

main_window = Tk()

main_window.geometry('800x600+50+50')
main_window.title('Welcome screen')

my_label = Label(main_window, text='My text', fg='white', bg='green')
# my_label.pack(fill=X)
# my_label.pack(fill=Y, expand = 1)
# my_label.pack(fill=BOTH, expand = 1)

red_label = Label(main_window, text='Red', fg='white', bg='red')
red_label.pack(fill=X, padx=10, ipadx=30, side=LEFT)

yellow_label = Label(main_window, text='Yellow', fg='black', bg='yellow')
yellow_label.pack(fill=X, pady=5, ipady=30, side=LEFT)

green_label = Label(main_window, text='Green', fg='white', bg='green')
green_label.pack(fill=X, padx=10, pady=10, side=LEFT)


list_box = Listbox(main_window)
list_box.pack()
# list_box.pack(fill=BOTH, expand=1)

for i in range(20):
    list_box.insert(END, str(i))
    # list_box.insert(i+1, str(i))

main_window.mainloop()
