from tkinter import *

FONT_NAME = 'Helvetica'

win = Tk()
win.title("Password Manager")
win.config(padx=20, pady=20)

canv = Canvas(width=200 , height=200)
logo = PhotoImage(file='passgen_img.png')
canv.create_image(100, 100, image=logo)
canv.grid(column=1, row=0)

# entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
# label
website_label = Label(text='Website:', font=(FONT_NAME, 12, 'normal'))
website_label.grid(column=0, row=1)
# entry
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
# label
email_label = Label(text='Email/Username:', font=(FONT_NAME, 12, 'normal'))
email_label.grid(column=0, row=2)
# entry
password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)
# label
password_label = Label(text='Password:', font=(FONT_NAME, 12, 'normal'))
password_label.grid(column=0, row=3)
# button
gen_password = Button(text='Generate Password', width=11)
gen_password.grid(column=2, row=3)
# button
add_button = Button(text='Add', width=32)
add_button.grid(column=1, row=4, columnspan=2)


win.mainloop()