from tkinter import *
from tkinter import font


root_window = Tk()

root_window.geometry('500x500')
root_window.title('Welcome screen')

hello_label = Label(root_window, text='Welcome to Tkinter!',
                    font=('arial', 20, 'bold'), fg='green', bg='yellow', relief='solid')
hello_label.pack()


virsion_label = Label(root_window, text='version 8.6',
                      font=('arial', 20, 'bold'), fg='green', bg='yellow', relief='solid')
virsion_label.pack()
# virsion_label.place(x=250, y=250)

go_button = Button(root_window, text='Go!',
                      font=('arial', 20, 'bold'), fg='green', bg='yellow', relief=RAISED)

go_button.pack()
# print(TkVersion)
# print(font.families())

root_window.mainloop()
