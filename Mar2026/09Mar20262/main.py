from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbol = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_number = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letter + password_symbol + password_number

    random.shuffle(password_list)

    password = "".join(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email_username = email_username_input.get()
    passwords = password_input.get()

    if len(website) == 0 or len(passwords) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title="website", message=f"These are the details entered: \nEmail: {email_username}\nPassword: {passwords}\nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{website} | {email_username} | {passwords}\n")
                
                website_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

# image
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
password_img = PhotoImage(file="logo.png")
# (100, 100) = center
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)

# words
website_word = Label(text="Website:", bg="white")
website_word.grid(column=0, row=1)

email_username_word = Label(text="Email/Username:", bg="white")
email_username_word.grid(column=0, row=2)

password_word = Label(text="Password:", bg="white")
password_word.grid(column=0, row=3)

# inputs
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2, sticky="W")
website_input.focus()

email_username_input = Entry(width=35)
email_username_input.grid(column=1, row=2, columnspan=2, sticky="W")
email_username_input.insert(0, "kaixiang980117@gmail.com")

password_input = Entry(width=21)
password_input.grid(column=1, row=3, columnspan=2, sticky="W")

# buttons
generate_password_button = Button(text="Generate Password", bg="white", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="W")

add_button = Button(text="Add", width=36, bg="white", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="W")

window.mainloop()