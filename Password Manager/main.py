from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="opps", message="please make sure no field is empty")
    else:
        is_okay = messagebox.askokcancel(title=website,
                                         message=f"These are the details entered:\n Email: {email} \n Password: {password}\n Is it Okay to Save? ")
        if is_okay:
            try:
                with open("data.json", "r") as data_file:
                   data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)

                with open("data.json", "w") as data_file:
                   json.dump(new_data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
           data =json.load(data_file)
    except:
          messagebox.showinfo(title="error", message="data file not found")
    else:
          if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="website",message=f"email: {email}\n password:{password}")
          else:
              messagebox.showinfo(title="error", message="no website details  found")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height = 200 ,width=200)
Photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=Photo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


website_entry = Entry(width=21)
website_entry.grid(row=1,column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.insert(0, "goyalravish2001@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

search_button = Button(text="search", width=13,command=find_password)
search_button.grid(row=1, column=2)
Generate_password_button = Button(text="Generate password", command=generate)
Generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()