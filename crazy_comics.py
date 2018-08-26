from tkinter import *

def update_label():
    comic_info.set("")
    for p in comics:
        comic_info.set(comic_info.get() + p._name + "    Comics Available:   " + str(p._amount) + "    Comics Sold:   " + str(p._sold) + "\n")

def update_menus():
    global comic_menu
    global restock_option
    global delete_option

    comic_menu.grid_forget()
    comic_menu = OptionMenu(info_frame, selected_comic, *comic_names)
    comic_menu.grid(row = 2, column = 0)

    restock_option.grid_forget()
    restock_option = OptionMenu(restock_frame, restock_name, *comic_names)
    restock_option.grid(row = 1, column = 1)

    delete_option.grid_forget()
    delete_option = OptionMenu(delete_frame, delete_name, *comic_names)
    delete_option.grid(row = 1, column = 1)     

def change_sold():
    for i in comics:
        try:
            if selected_comic.get() == i._name:
                if int(num_comics.get()) >= 1 and int(num_comics.get()) <= i._amount:
                    i._amount -= int(num_comics.get())
                    i._sold += int(num_comics.get())
                    error_msg.set("Successfully sold {} {} comic(s)".format(int(num_comics.get()), i._name))

                elif int(num_comics.get()) < 1:
                    error_msg.set("Please enter a value that is larger than 0!")

                elif int(num_comics.get()) > i._amount:
                    error_msg.set("Please enter a value that is {} or less!".format(i._amount))

        except ValueError:
            error_msg.set("Please enter an integer value!")

    update_label()

def add_comic():
    try:
        if add_name.get() == '':
            add_error_msg.set("Please enter a value for the comic name!")
        elif int(add_amount.get()) < 1:
            add_error_msg.set("Please enter a value that is larger than 1!")
        else:
            Comics(add_name.get(), int(add_amount.get()), 0)
            update_label()
            add_error_msg.set("")
            update_menus()
    except ValueError:
        add_error_msg.set("Please type in an integer value!")

def restock_comic():
    for i in comics:
        try:
            if restock_name.get() == i._name:
                if int(restock_amount.get()) >= 1 and int(restock_amount.get()) <= 20:
                    i._amount += int(restock_amount.get())
                    restock_error_msg.set("Successfully restocked {} {} comic(s)".format(int(restock_amount.get()), i._name))

                elif int(restock_amount.get()) < 1:
                    restock_error_msg.set("Please enter a value that is larger than 0!")

                elif int(restock_amount.get()) > 20:
                    restock_error_msg.set("Please enter a value that is 20 or less!")

        except ValueError:
            restock_error_msg.set("Please enter an integer value!")

    update_label()

def delete_comic():
    for i in comics:
        if delete_name.get() == i._name:
            comics.remove(i)
            comic_names.remove(i._name)
            update_label()
            update_menus()

class Comics:
    def __init__(self, name, amount, sold):
        self._name = name 
        self._amount = amount
        self._sold = sold
        comics.append(self)
        comic_names.append(self._name)

comics = []
comic_names = []

Comics("Python Panic", 8, 0)
Comics("Scrath the Cat", 12, 0)
Comics("Tony Tkinter", 3, 0)


root = Tk()
root.title("comics label")
root.geometry('800x1000')

info_frame = Frame(root, relief = "groove", borderwidth = 2, width = 400, height = 800)
info_frame.grid_propagate(0)
info_frame.grid(rowspan = 4, column = 0)
add_frame = Frame(root, relief = "groove", borderwidth = 2, width = 400)
#add_frame.grid_propagate(0)
add_frame.grid(row = 0, column = 1)
restock_frame = Frame(root, relief = "groove", borderwidth = 2, width = 400)
restock_frame.grid(row = 1, column = 1)
delete_frame = Frame(root, relief = "groove", borderwidth = 2, width = 400)
delete_frame.grid(row = 2, column = 1)
frame5 = Frame(root, relief = "groove", borderwidth = 2, width = 400).grid(row = 2, column = 1)



comic_info = StringVar()

comic_lbl = Label(info_frame, textvariable=comic_info)
comic_lbl.grid(row = 0, columnspan = 2)

selling_window = Label(info_frame, text = "Selling Window")
selling_window.grid(row = 1, columnspan = 2)

quantity_sold = Label(info_frame, text = "Quantity Sold")
quantity_sold.grid(row = 2, column = 0)

selected_comic = StringVar()
selected_comic.set(comic_names[0])

comic_menu = OptionMenu(info_frame, selected_comic, *comic_names)
comic_menu.grid(row = 2, column = 0)

num_comics = StringVar()

comic_entry = Entry(info_frame, textvariable=num_comics)
comic_entry.grid(row = 2, column = 1)

select_btn = Button(info_frame, text="Select", command=change_sold)
select_btn.grid(row = 3, columnspan = 2)

error_msg = StringVar()
error_msg.set("")

selling_error = Label(info_frame, textvariable=error_msg)
selling_error.grid(row=3, column = 1)

add_window = Label(add_frame, text="Adding Window")
add_window.grid(row = 0, columnspan = 2)

name_lbl = Label(add_frame, text = "Name ")
name_lbl.grid(row = 1, column = 0)

add_name = StringVar()

add_entry = Entry(add_frame, textvariable=add_name)
add_entry.grid(row = 1, column = 1)

amount_lbl = Label(add_frame, text = "Quantity ")
amount_lbl.grid(row = 2, column = 0)

add_amount = StringVar()

amount_entry = Entry(add_frame, textvariable=add_amount)
amount_entry.grid(row = 2, column = 1)

add_btn = Button(add_frame, text="Select", command=add_comic)
add_btn.grid(row = 3, columnspan = 2)

add_error_msg = StringVar()
add_error_msg.set("")

add_error = Label(add_frame, textvariable=add_error_msg)
add_error.grid(row= 4 , columnspan = 2)

'''Restock stuff'''

restock_window = Label(restock_frame, text="Restock Window")
restock_window.grid(row = 0, columnspan = 2)



restock_name_lbl = Label(restock_frame, text = "Name ")
restock_name_lbl.grid(row = 1, column = 0)

restock_name = StringVar()
restock_name.set(comic_names[0])

restock_option = OptionMenu(restock_frame, restock_name, *comic_names)
restock_option.grid(row = 1, column = 1)

restock_amount_lbl = Label(restock_frame, text = "Quantity ")
restock_amount_lbl.grid(row = 2, column = 0)

restock_amount = StringVar()

restock_amount_entry = Entry(restock_frame, textvariable=restock_amount)
restock_amount_entry.grid(row = 2, column = 1)

restock_btn = Button(restock_frame, text="Select", command=restock_comic)
restock_btn.grid(row = 3, columnspan = 2)

restock_error_msg = StringVar()
restock_error_msg.set("")

restock_error = Label(restock_frame, textvariable=restock_error_msg)
restock_error.grid(row= 4 , columnspan = 2)

'''Delete Stock'''

restock_window = Label(restock_frame, text="Restock Window")
restock_window.grid(row = 0, columnspan = 2)


restock_name_lbl = Label(restock_frame, text = "Name ")
restock_name_lbl.grid(row = 1, column = 0)

restock_name = StringVar()
restock_name.set(comic_names[0])

restock_option = OptionMenu(restock_frame, restock_name, *comic_names)
restock_option.grid(row = 1, column = 1)

restock_btn = Button(restock_frame, text="Select", command=restock_comic)
restock_btn.grid(row = 3, columnspan = 2)

restock_error_msg = StringVar()
restock_error_msg.set("")

restock_error = Label(restock_frame, textvariable=restock_error_msg)
restock_error.grid(row= 4 , columnspan = 2)

'''Delete Stuff'''

restock_window = Label(restock_frame, text="Restock Window")
restock_window.grid(row = 0, columnspan = 2)



restock_name_lbl = Label(restock_frame, text = "Name ")
restock_name_lbl.grid(row = 1, column = 0)

restock_name = StringVar()
restock_name.set(comic_names[0])

restock_option = OptionMenu(restock_frame, restock_name, *comic_names)
restock_option.grid(row = 1, column = 1)

restock_amount_lbl = Label(restock_frame, text = "Quantity ")
restock_amount_lbl.grid(row = 2, column = 0)

restock_amount = StringVar()

restock_amount_entry = Entry(restock_frame, textvariable=restock_amount)
restock_amount_entry.grid(row = 2, column = 1)

restock_btn = Button(restock_frame, text="Select", command=restock_comic)
restock_btn.grid(row = 3, columnspan = 2)

restock_error_msg = StringVar()
restock_error_msg.set("")

restock_error = Label(restock_frame, textvariable=restock_error_msg)
restock_error.grid(row= 4 , columnspan = 2)

'''Delete Stock'''

delete_window = Label(delete_frame, text="delete Window")
delete_window.grid(row = 0, columnspan = 2)


delete_name_lbl = Label(delete_frame, text = "Name ")
delete_name_lbl.grid(row = 1, column = 0)

delete_name = StringVar()
delete_name.set(comic_names[0])

delete_option = OptionMenu(delete_frame, delete_name, *comic_names)
delete_option.grid(row = 1, column = 1)

delete_btn = Button(delete_frame, text="Select", command=delete_comic)
delete_btn.grid(row = 3, columnspan = 2)

delete_error_msg = StringVar()
delete_error_msg.set("")

delete_error = Label(delete_frame, textvariable=delete_error_msg)
delete_error.grid(row= 4 , columnspan = 2)

update_label()
root.mainloop()