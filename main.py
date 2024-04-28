from tkinter import *
from tkinter import messagebox
import random
import pyperclip

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
    url = url_entry.get()
    user_id = id_entry.get()
    password = password_entry.get()

    if len(url) == 0 or len(user_id) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Pleas don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title="url",
                                       message=f"These are the details entered:\nEmail: {user_id}\nPassword: {password}\nIs it OK to save?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{url}, {user_id}, {password}\n")
            url_entry.delete(0, END)
            password_entry.delete(0, END)
            url_entry.focus()
            messagebox.showinfo(title="", message="completed!")


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
url_entry = Entry(width=35, font=(FONT_NAME, 12))
url_entry.grid(column=1, row=1, columnspan=2)
url_entry.focus()

id_entry = Entry(width=35, font=(FONT_NAME, 12))
id_entry.grid(column=1, row=2, columnspan=2)
id_entry.insert(END, "may_e_mail@address.com")

password_entry = Entry(width=22, font=(FONT_NAME, 12))
password_entry.grid(column=1, row=3)

# buttons
generate_button = Button(text="Generate Password", width=17, font=(FONT_NAME, 9), command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=49, font=(FONT_NAME, 9), command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
