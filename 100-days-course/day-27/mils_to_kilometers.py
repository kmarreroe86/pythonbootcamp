from tkinter import *


MILES_TO_KILOMETERS_FACTOR = 1.609344
window = Tk()
window.title("Mi to Km Converter")
window.minsize(width=500, height=200)
window.config(padx=20, pady=20)

def calculate_action():
    print("calculate_action")
    miles = float(input.get())
    km = round(miles * MILES_TO_KILOMETERS_FACTOR, 3)
    result_label.config(text=km)



input = Entry(width=7)
input.grid(column=1, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0,row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

result_label = Label(text="0")
result_label.grid(column=1,row=1)

km_label = Label(text="Km")
km_label.grid(column=2,row=1)

calculate_btn = Button(text="Calculate", command=calculate_action)
calculate_btn.grid(column=1, row=2)

window.mainloop()
