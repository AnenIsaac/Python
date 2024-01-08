# import tkinter

# # Window
# window = tkinter.Tk()
# window.title("GUI Program")
# window.minsize(width=500, height=300)

# # Label
# my_label = tkinter.Label(text="Label", font=("Arial", 24, "bold"))
# my_label.pack()

# my_label["text"] = "New Text"
# my_label.config(text="New Text")


# # Button
# def button_clicked():
#     my_label.config(text=text_entry.get())


# button = tkinter.Button(text="Click Me", command=button_clicked)
# button.pack()

# # Entry
# text_entry = tkinter.Entry(width=10)
# text_entry.pack()

# # Text
# text = tkinter.Text(height=5, width=30)
# # Puts cursor in textbox
# text.focus()
# # Adds some text to begin with.
# text.insert(tkinter.END, "Example of multi-line text entry.")
# # Get the current value in the textbox
# print(text.get("1.0", tkinter.END))
# text.pack()


# # checkbutton
# def checkbutton_used():
#     # prints 1 if On button checked, otherwise 0
#     print(checked_state.get())


# # variable to hold on to checked state, 0 is off, 1 is on
# checked_state = IntVar()
# checkbutton = Checkbutton(
#     text="Is On", variable=checked_state, command=checkbutton_used
# )
# window.mainloop()
