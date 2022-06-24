from tkinter import *

root = Tk()

root.geometry('500x300+100+100')

# red_label = Label(root, text='Red', fg='white', bg='red')
# red_label.place(x=150, y=250, width=200)

# yellow_label = Label(root, text='Yellow', fg='black', bg='yellow')
# yellow_label.place(x=175, y=130, width=150, height=40)

# green_label = Label(root, text='Green', fg='white', bg='green')
# green_label.place(x=100, y=135, height=30)

# red_label_rel_height = Label(
#     root, text='Red relheight=0.3', fg='white', bg='red')
# red_label_rel_height.place(relheight=0.3)

# yellow_label_rel_width = Label(
#     root, text='Yellow relwidth=0.7', fg='black', bg='yellow')
# yellow_label_rel_width.place(relwidth=0.7)

# green_label_rel_x = Label(root, text='Green relx=0.2', fg='white', bg='green')
# green_label_rel_x.place(relx=0.2)

# green_label_rel_y = Label(root, text='Green rely=0.4', fg='white', bg='green')
# green_label_rel_y.place(rely=0.4)

label = Label(
    root, text='Some text', fg='white', bg='green')
label.place(width=400, height=100, x=50, y=100)

button = Button(
    root, text='Some button')
button.place(in_=label, relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
