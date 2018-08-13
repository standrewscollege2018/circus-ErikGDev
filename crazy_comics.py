from tkinter import *

def update_label():
    comic_info.set("")
    for p in comics:
        comic_info.set(comic_info.get() + p._name + "    Comics Available:  " + str(p._amount) + "\n")

def change_sold():
    print("Hello")

class Comics:
    def __init__(self, name, amount):
        self._name = name 
        self._amount = amount
        comics.append(self)
        comic_names.append(self._name)

comics = []
comic_names = []

Comics("Python Panic", 8)
Comics("Scrath the Cat", 12)
Comics("Tony Tkinter", 3)


root = Tk()
root.title("comics label")
root.geometry('800x1000')

info_frame = Frame(root, relief = "groove", borderwidth = 2, width = 800, height = 100)
info_frame.grid(row = 0)
frame2 = Frame(root, relief = "groove", borderwidth = 2, width = 400).grid(row = 1, column = 0)
frame3 = Frame(root, relief = "groove", borderwidth = 2, width = 400).grid(row = 1, column = 1)
frame4 = Frame(root, relief = "groove", borderwidth = 2, width = 400).grid(row = 2, column = 0)
frame5 = Frame(root, relief = "groove", borderwidth = 2, width = 400).grid(row = 2, column = 1)



comic_info = StringVar()

comic_lbl = Label(info_frame, textvariable=comic_info)
comic_lbl.grid(row=0, column = 0)

selling_window = Label(info_frame, text = "Selling Window")
selling_window.grid(row=0, column = 1)

quantity_sold = Label(info_frame, text = "Quantity Sold")
quantity_sold.grid(row=0, column = 2)

selected_comic = StringVar()
selected_comic.set(comic_names[0])

comic_menu = OptionMenu(info_frame, selected_comic, *comic_names)
comic_menu.grid(row=1, column = 1)

num_comics = StringVar()

comic_entry = Entry(info_frame, textvariable=num_comics)
comic_entry.grid(row=1, column = 2)

select_btn = Button(info_frame, text="Select", command=change_sold)
select_btn.grid(row=2, column = 1)

update_label()
root.mainloop()