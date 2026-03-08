from tkinter import *

def miles_to_km():
    # 拿到下面的那个被input 的数字
    miles = float(input.get())
    km = miles * 1.609
    km_num.config(text=f"{km}")

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# label

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_num = Label(text="0")
km_num.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# entry
input = Entry(width=7)
input.grid(column=1, row=0)

# button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()