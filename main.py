from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT_NAME = 'Helvetica'


def save_entry():
    website_text = website_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()
    
    new_data = {
        website_text: {
            'email': email_text,
            'password': password_text
        }
    }
    
    if len(website_text) == 0 or len(email_text) == 0 or len(password_text) == 0:
        messagebox.showinfo(title='Invalid entry', message='Please fill out all of the fields')
    else:
        try:
            with open('password_bank.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open('password_bank.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open('password_bank.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        finally:
            clear_text()
            
                    
def clear_text():
    website_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)
    

def create_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        
    letter_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    number_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    symbol_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    
    password_list = letter_list + number_list + symbol_list
    random.shuffle(password_list)

    password = "".join(password_list)
        
    password_entry.insert(0, password)
    pyperclip.copy(password)
    

def search_bank():
    pass
        

win = Tk()
win.title("Password Manager")
win.config(padx=20, pady=20)

canv = Canvas(width=200 , height=200)
logo = PhotoImage(file='passgen_img.png')
canv.create_image(100, 100, image=logo)
canv.grid(column=1, row=0, columnspan=2, padx=(0, 80))

website_entry = Entry(width=20)
website_entry.grid(column=1, row=1)
website_entry.focus()

search_button = Button(text='Search', width=11, command=search_bank)
search_button.grid(column=2, row=1)

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

gen_password = Button(text='Generate Password', width=11, command=create_pass)
gen_password.grid(column=2, row=3)

add_button = Button(text='Add', width=32, command=save_entry)
add_button.grid(column=1, row=4, columnspan=2)


win.mainloop()