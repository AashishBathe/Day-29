from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    password_input.delete(0, END)
    # Pass Generator from Day 5.
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]
    number_list = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = letter_list + symbol_list + number_list
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pass():
    password = password_input.get()
    website = website_input.get()
    email = email_input.get()
    new_data = {
        website.title(): {
            "email": email,
            "password": password
        }
    }
    if len(password) == 0 or len(website) == 0 or len(email) == 0:
        messagebox.showerror(title="Oops", message="Please do not leave any fields empty!")
    else:
        try:
            with open("data.json", mode='r') as file:
                pass
            # json.dump(new_data, file, indent=4) # Write data to json file

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump({}, file)

        finally:
            with open("data.json", "r") as file:
                # Reading old data
                data = json.load(file)
                # Updating old data with new data
                data.update(new_data)

            with open("data.json", mode='w') as file:
                # Saving updated data
                json.dump(data, file, indent=4)
                website_input.delete(0, 'end')
                password_input.delete(0, 'end')
                website_input.focus()

# ------------------------- SEARCH PASSWORD ---------------------------- #


def search():
    try:
        with open("data.json", "r") as file:
            pass
    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="File does not exist.")
    else:
        website = website_input.get()
        with open("data.json", "r") as file:
            data = json.load(file)
            if website.title() in data:
                for item in data:
                    if website.title() == item:
                        pyperclip.copy(data[item]["password"])
                        messagebox.showinfo(title=item, message=f"Email: {data[item]['email']}"
                                                                   f"\nPassword: {data[item]['password']}")
            else:
                messagebox.showerror(title="Oops", message="No existing data.")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)
website_text = Label(text="Website:")
website_text.grid(row=1, column=0, sticky=E)
email_text = Label(text="Email/Username:")
email_text.grid(row=2, column=0, sticky=E)
password_text = Label(text="Password:")
password_text.grid(row=3, column=0, sticky=E)
website_input = Entry()
website_input.focus()
website_input.grid(row=1, column=1, sticky=EW)
email_input = Entry(width=52)
email_input.insert(0, "aashish@gmail.com")
email_input.grid(row=2, column=1, columnspan=2, sticky=EW)
password_input = Entry()
password_input.grid(row=3, column=1, sticky=EW)
generate_button = Button(text="Generate Password", command=generate_pass)
generate_button.grid(row=3, column=2)
search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2, sticky=EW)
add_button = Button(text="Add", command=add_pass)
add_button.grid(row=4, column=1, columnspan=2, sticky=EW)

window.mainloop()
