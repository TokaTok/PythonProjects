from tkinter import *


def calculate_fahrenheit():
    fahrenheit_entry.delete(0, END)
    num = float(celsius_entry.get())
    num = num * 9 / 5 + 32
    fahrenheit_entry.insert(0, num)


def calculate_celsius():
    celsius_entry.delete(0, END)
    num = float(fahrenheit_entry.get())
    num = num * 5 / 9 - 32
    celsius_entry.insert(0, num)


window = Tk()
window.title("Convert F to C or C to F")
window.config(pady=10)

text_fahr = StringVar()
text_fahr.trace("w", calculate_fahrenheit)

fahrenheit_label = Label(text="Fahrenheit")
fahrenheit_label.grid(row=0, column=1, padx=100, pady=5)

celsius_label = Label(text="Celsius")
celsius_label.grid(row=0, column=2, padx=100, pady=5)

fahrenheit_entry = Entry(width=20)
fahrenheit_entry.insert(END, "0")
fahrenheit_entry.grid(row=1, column=1, padx=100, pady=5)

celsius_entry = Entry(width=20)
celsius_entry.insert(END, "0")
celsius_entry.grid(row=1, column=2, padx=100, pady=5)

calculate_farh_button = Button(text="Calculate Celsius", width=20, pady=5, command=calculate_celsius())
calculate_farh_button.grid(row=2, column=1)

calculate_cel_button = Button(text="Calculate Fahrenheit", width=20, pady=5, command=calculate_fahrenheit)
calculate_cel_button.grid(row=2, column=2)

window.mainloop()
