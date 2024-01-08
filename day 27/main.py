import tkinter

# Window
window = tkinter.Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button
def button_clicked():
    my_label.config(text=text_entry.get())


button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
text_entry = tkinter.Entry(width=10)
text_entry.pack()

window.mainloop()
