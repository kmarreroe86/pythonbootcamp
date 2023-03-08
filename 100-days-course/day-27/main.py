import tkinter

window = tkinter.Tk()
window.title("My first UI programm")
window.minsize(width=500, height=300)


# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0,row=0)

# Button
def button_clicked() -> None:
    print("Button cliked!")
    my_label.config(text=input.get())

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)
# button.pack()

new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry
input = tkinter.Entry(width=10)
# input.get() => get text written
# input.pack()
input.grid(column=1, row=2)


window.mainloop()
