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

#Text Entry Box
text = Text(height=5, width=30)
#Starts with cursor in text box
text.focus()
#Adds sample starter text
text.insert(END, "Sample multiline text entry.")
#Get's current value of text entry starting at line 1 character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #Get's the current value in spinbox
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value
def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #1 if button is on or 0 if off
    print(checked_state.get())

#variable to hold on to checked state, 0 is off 1 is on
checked_state = IntVar()
checkbutton = Checkbutton(text="Is on?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radiobutton_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radiobutton_used)
radiobutton2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radiobutton_used)
radiobutton1.pack()
radiobutton2.pack()

#Listbox
def listbox_used(event):
    #Gets current selection of listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Banana", "Orange"]
for fruit in fruits:
    listbox.insert(fruits.index(fruit), fruit)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()