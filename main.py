from tkinter import *
from tkinter import messagebox

FONT_NAME = 'Helvetica'


def save_entry():
    website_text = website_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()
    if len(website_text) != 0 and len(email_text) != 0 and len(password_text) != 0:
        is_correct = messagebox.askokcancel(message=f"Would you like to save this entry?:\n\nWebsite: {website_text}\nEmail: {email_text}\nPassword: {password_text}\n")
        if is_correct:
            file = open('password_bank.txt', 'a')
            file.write(f"{website_text} | {email_text} | {password_text}\n")
            file.close()
            clear_text()
    else:
        messagebox.showinfo(title='Invalid entry', message='Please fill out all of the fields')
    

def clear_text():
    website_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)


win = Tk()
win.title("Password Manager")
win.config(padx=20, pady=20)

canv = Canvas(width=200 , height=200)
logo = PhotoImage(file='passgen_img.png')
canv.create_image(100, 100, image=logo)
canv.grid(padx=(40, 0), pady=(0, 0), column=1, row=0)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

website_label = Label(text='Website:', font=(FONT_NAME, 12, 'normal'))
website_label.grid(column=0, row=1)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)

email_label = Label(text='Email/Username:', font=(FONT_NAME, 12, 'normal'))
email_label.grid(column=0, row=2)

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

password_label = Label(text='Password:', font=(FONT_NAME, 12, 'normal'))
password_label.grid(column=0, row=3)

gen_password = Button(text='Generate Password', width=11)
gen_password.grid(column=2, row=3)

add_button = Button(text='Add', width=32, command=save_entry)
add_button.grid(column=1, row=4, columnspan=2)


win.mainloop()