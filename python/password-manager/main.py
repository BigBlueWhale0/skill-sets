from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
FONT_NAME = "Courier"

def search_password():
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
        website_name = website_entry.get()
        messagebox.showinfo(title="Info", message=f"Email: {data[website_name]["email"]} \nPassword: {data[website_name]["password"]}")
    except FileNotFoundError:
        messagebox.showinfo(title="Info", message="No Data File Found")
    except KeyError:
        messagebox.showinfo(title="Info", message="No details for the website exists")


def generate_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

def save_password():
    website_name = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website_name: {
            "email": email,
            "password": password,
        }
    }
    if validate():
        is_ok = messagebox.askokcancel(title=website_name,message=f"These are the details entered \nEmail: {email} "
                                                          f"\nPassword: {password} \nIs it Ok to save? ")
        if is_ok:
            try:
                with open("data.json",mode="r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')

def validate():
    is_ok = True
    if len(website_entry.get()) == 0:
        messagebox.showinfo(title="Info",message="Website name can't be empty")
        is_ok = False
    if len(email_entry.get()) == 0:
        messagebox.showinfo(title="Info",message="Email can't be empty")
        is_ok = False
    if len(password_entry.get()) == 0:
        messagebox.showinfo(title="Info",message="Password can't be empty")
        is_ok = False
    return is_ok

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200,highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=0,row=0,columnspan=3)

generate_button = Button(text="Generate Password",width=20, highlightthickness=0,command=generate_password)
generate_button.grid(column=2,row=3)
add_button = Button(text="Add", width=35, highlightthickness=0,command=save_password)
add_button.grid(column=1,row=4,columnspan=2)
search_button = Button(text="Search", width=20, highlightthickness=0,command=search_password)
search_button.grid(column=2,row=1)

website_label = Label(text="Website:", font=(FONT_NAME, 15),justify="left")
website_label.grid(column=0,row=1)
email_label = Label(text="Email/Username:", font=(FONT_NAME, 15),justify="left")
email_label.grid(column=0,row=2)
password_label = Label(text="Password:", font=(FONT_NAME, 15),justify="left")
password_label.grid(column=0,row=3)

website_entry = Entry(width=15,fg="white")
website_entry.grid(column=1,row=1)
website_entry.focus()
email_entry = Entry(width=40,fg="white")
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0, "example@gmail.com")
password_entry = Entry(width=15,fg="white")
password_entry.grid(column=1,row=3)

window.mainloop()