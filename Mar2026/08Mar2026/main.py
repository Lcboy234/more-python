from tkinter import *

def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())

window = Tk()
window.title("My First GUI Program")
window.minsize(width = 500, height = 300)
window.config(padx=50, pady=50)

# label
my_label = Label(text="I am a label", font=("Arial", 24, "italic"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

# button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# new_button
button_2 = Button(text="New Button")
button_2.grid(column=2, row=0)

# entry
input = Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()