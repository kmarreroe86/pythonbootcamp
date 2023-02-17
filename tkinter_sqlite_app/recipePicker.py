import tkinter
import tkinter as tk
import sqlite3
from PIL import ImageTk
from numpy import random

BACKGROUND_COLOR = "#3d6466"
# initiallize app(lunches the window)
root = tk.Tk()
root.title("Recipe Picker")
root.eval("tk::PlaceWindow . center")

frame1 = tk.Frame(root, width=500, height=600, bg=BACKGROUND_COLOR)
frame2 = tk.Frame(root, bg=BACKGROUND_COLOR)

for frame in (frame1, frame2):
    frame.grid(row=0, column=0, sticky="nesw") # sticky="nesw" -> north east, south, west


def fetch_db():
    connection = sqlite3.connect("data/recipes.db")
    cursor = connection.cursor()
    cursor.execute("select * from sqlite_schema where type='table';")
    all_tables = cursor.fetchall()

    idx = random.randint(0, len(all_tables) - 1)
    print(all_tables[idx])

    # fetch ingredients
    table_name = all_tables[idx][1]
    cursor.execute(f"select * from {table_name};")
    table_records = cursor.fetchall()
    print(table_records)

    connection.close()
    return table_name, table_records


def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def pre_process(table_name, table_records):
    title = table_name[:-6]
    title = "".join(
        [char if char.islower() else " " + char for char in title]
    ).strip()
    print(title)

    # ingredients
    ingredients = []
    for record in table_records:
        name = record[1]
        qty = record[2]
        unit = record[3]
        ingredients.append(qty + " " + unit + " " + name)

    return title, ingredients


def load_frame1():
    clear_widgets(frame2)
    frame1.tkraise()
    frame1.pack_propagate(False)

    # create frame widget
    logo_img = ImageTk.PhotoImage(file="assets/RRecipe_logo.png")
    logo_widget = tk.Label(frame1, image=logo_img, bg=BACKGROUND_COLOR)
    logo_widget.image = logo_img
    logo_widget.pack()

    # button widget
    tk.Button(
        frame1,
        text="SHUFFLE",
        font=("TkHeadingFont", 20),
        # bg="#28393a", #3d6466
        bg="#3d6466",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: load_frame2()
    ).pack(pady=20)

    tk.Label(
        frame1,
        text="ready for your random recipe?",
        bg=BACKGROUND_COLOR,
        fg="white",
        font=("TkMenuFont", 14)
    ).pack()


def load_frame2():
    clear_widgets(frame1)
    frame2.tkraise()
    table_name, table_records = fetch_db()
    title, ingredients = pre_process(table_name, table_records)

    logo_img = ImageTk.PhotoImage(file="assets/RRecipe_logo_bottom.png")
    logo_widget = tk.Label(frame2, image=logo_img, bg=BACKGROUND_COLOR)
    logo_widget.image = logo_img
    logo_widget.pack(pady=20)

    tk.Label(
        frame2,
        text=title,
        bg=BACKGROUND_COLOR,
        fg="white",
        font=("TkHeadingFont", 14)
    ).pack(pady=25)

    for ingredient in ingredients:
        tk.Label(
            frame2,
            text=ingredient,
            bg=BACKGROUND_COLOR,
            fg="white",
            font=("TkMenuFont", 12)
        ).pack()

    tk.Button(
        frame2,
        text="BACK",
        font=("TkHeadingFont", 18),
        bg="#3d6466",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: load_frame1()
    ).pack(pady=20)


load_frame1()

# run app
root.mainloop()
