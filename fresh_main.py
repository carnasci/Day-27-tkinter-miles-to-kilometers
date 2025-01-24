from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = user_input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I am a label", font=("Arial", 20, "bold"))
my_label.config(text="New text")
my_label.pack()

#Button
button = Button(text="I am a button", command=button_clicked)
button.pack()

#Entry
user_input = Entry(width=10)
print(user_input.get())
user_input.pack()
window.mainloop()