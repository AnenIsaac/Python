from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip 
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# Password Generator Project
def generate_password():
    letters = ["a", "b", "c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B", "C","D","E","F","G","H","I","J","K","L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Missing Information",
            message="Please make sure you've filled all " "the necessary fields.",
        )
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered: \nEmail: {email}"
            f"\nPassword: {password} \nIs it OK to save?",
        )
        if is_ok:
            with open("passwords.txt", "a") as f:
                f.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# lock
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# website
website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)

website_entry = Entry(width=53)
website_entry.grid(column=1, row=1, columnspan=2)

# Email
email_label = Label(text="Email/Username:", bg="white")
email_label.grid(
    column=0,
    row=2,
)
email_entry = Entry(width=53)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "anen@email.com")

# Password
password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)
password_entry = Entry(width=35)
password_entry.grid(
    column=1,
    row=3,
)

# Buttons
generate_password_button = Button(
    text="Generate Password", bg="white", command=generate_password
)
generate_password_button.grid(
    column=2,
    row=3,
)
add_button = Button(text="Add", width=45, bg="white", command=save)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()
