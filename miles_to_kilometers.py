from tkinter import *

MULTIPLIER = 1.60934

window = Tk()
window.title("Miles Converter")
window.config(padx=30, pady=30)

def calculate_kilos():
    miles = float(user_miles.get())
    kilos = round(miles * MULTIPLIER)
    output_kilos.config(text=kilos)


user_miles = Entry(width=10)
user_miles.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 20))
miles_label.grid(column=2, row=0)

equal_to_label = Label(text="is equal to ", font=("Arial", 20))
equal_to_label.grid(column=0, row=1)

output_kilos = Label(text=0)
output_kilos.grid(column=1, row=1)

kilos_label = Label(text="Km", font=("Arial", 20))
kilos_label.grid(column=2, row=1)

calculate = Button(text="Calculate", command=calculate_kilos)
calculate.grid(column=1, row=2)

window.mainloop()