from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = url_entry.get()
    email = id_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Pleas don't leave any fields empty!")

    else:
        # is_ok = messagebox.askokcancel(title="url",
        #                                message=f"These are the details entered:\nEmail: {user_id}\nPassword: {password}\nIs it OK to save?")
        # if is_ok:

        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            url_entry.delete(0, END)
            password_entry.delete(0, END)
            url_entry.focus()
            messagebox.showinfo(title="", message="completed!")


def find_password():
    website = url_entry.get()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message="No details for the website exists")


# ---------------------------- UI SETUP ------------------------------- #
# display window
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=60)

# setting image
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# labels
url_label = Label(text="Website:", font=(FONT_NAME, 12))
url_label.grid(column=0, row=1)

id_label = Label(text="Email/Username:", font=(FONT_NAME, 12))
id_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=(FONT_NAME, 12))
password_label.grid(column=0, row=3)

# entries
url_entry = Entry(width=22, font=(FONT_NAME, 12))
url_entry.grid(column=1, row=1)
url_entry.focus()

id_entry = Entry(width=35, font=(FONT_NAME, 12))
id_entry.grid(column=1, row=2, columnspan=2)
id_entry.insert(END, "my_e_mail@address.com")

password_entry = Entry(width=22, font=(FONT_NAME, 12))
password_entry.grid(column=1, row=3)

# buttons
generate_button = Button(text="Generate Password", width=17, font=(FONT_NAME, 9), command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=49, font=(FONT_NAME, 9), command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=17, font=(FONT_NAME, 9), command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
