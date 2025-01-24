from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=500)

#Label
my_label = Label(text="I am a label", font=("Arial", 20, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

#Button
def button_clicked():
    my_label["text"] = user_input.get()


button = Button(text="Click Me", command=button_clicked)
button.pack()

#Entry
user_input = Entry(width=10)
user_input.pack()

window.mainloop()