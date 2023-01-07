from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pass():
    with open("data.txt", mode='a') as file:
        file.write(f"{website_input.get()} | {email_input.get()} | {password_input.get()}\n")
    website_input.delete(0, 'end')
    password_input.delete(0, 'end')
    website_input.focus()
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
website_input.grid(row=1, column=1, columnspan=2, sticky=EW)
email_input = Entry(width=52)
email_input.insert(0, "aashish@gmail.com")
email_input.grid(row=2, column=1, columnspan=2, sticky=EW)
password_input = Entry()
password_input.grid(row=3, column=1, sticky=EW)
generate_button = Button(text="Generate Password", command=generate_pass)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", command=add_pass)
add_button.grid(row=4, column=1, columnspan=2, sticky=EW)

window.mainloop()
