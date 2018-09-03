from tkinter import *
from tkinter import messagebox

#Create function to update the main label with stringVar comic_info
def update_label():
    comic_info.set("")
    #Loop through each comic and print out its information
    for p in comics:
        comic_info.set(comic_info.get() + p._name + "    Comics Available:   " + str(p._amount) + "    Comics Sold:   " + str(p._sold) + "\n")

#Create function to update the tkinter optionMenus
def update_menus():
    #Globalise every option menu
    global comic_menu
    global restock_option
    global delete_option

    #Update comic_menu to its new values
    selected_comic.set(comic_names[0])
    comic_menu.grid_forget()
    comic_menu = OptionMenu(info_frame, selected_comic, *comic_names)
    comic_menu.grid(row = 2, column = 0)

    #Update restock_option to its new values
    restock_name.set(comic_names[0])
    restock_option.grid_forget()
    restock_option = OptionMenu(restock_frame, restock_name, *comic_names)
    restock_option.grid(row = 1, column = 1)

    #Update delete_option to its new values
    delete_name.set(comic_names[0])
    delete_option.grid_forget()
    delete_option = OptionMenu(delete_frame, delete_name, *comic_names)
    delete_option.grid(row = 1, column = 1)     

#Create Function for selling window, which changes amount sold and amount left of comics
def change_sold():
    #Loop through comics
    for i in comics:
        try:
            #If the comic selected is the looped comic
            if selected_comic.get() == i._name:
                #If the number entered by the user is between 1 and the amount left
                if int(num_comics.get()) >= 1 and int(num_comics.get()) <= i._amount:
                    #Change amount sold and amount left using sell_comic() and sell_number() functions
                    i.sell_comic(int(num_comics.get()))
                    i.sell_number(int(num_comics.get()))

                    #Set error message to success
                    error_msg.set("Successfully sold {} {} comic(s)".format(int(num_comics.get()), i._name))
                
                #If the value is less than 1
                elif int(num_comics.get()) < 1:
                    error_msg.set("Please enter a value that is larger than 0!")

                #If the value is larger than the amount left in stock
                elif int(num_comics.get()) > i._amount:
                    error_msg.set("Please enter a value that is {} or less!".format(i._amount))

        #If the value is not an integer
        except ValueError:
            error_msg.set("Please enter an integer value!")

    #Run update_label() function to update the main label
    update_label()

'''
The function add_comic() is used to add a new comic to the lists of comics. If the values of the
names and the comic amount are appropriate, add another instance of the Comics class, otherwise
show error messages to display to the user what is wrong
'''
def add_comic():
    try:
        if add_name.get() == '':
            add_error_msg.set("Please enter a value for the comic name!")
        elif int(add_amount.get()) < 1:
            add_error_msg.set("Please enter a value that is larger than 0!")
        elif int(add_amount.get()) > 20:
            add_error_msg.set("Please enter a value that is less than 20!")
        elif add_name.get() in comic_names:
            add_error_msg.set("This comic already exists in the inventory!")
        else:
            Comics(add_name.get(), int(add_amount.get()), 0)
            update_label()
            add_error_msg.set("")
            update_menus()
    except ValueError:
        add_error_msg.set("Please type in an integer value!")

'''
The function restock_comic() is used to restock the amount of a comic. First we loop through the comics.
after a comic in the loop is equal to the name entered, we restock the comic based on the user's input. If
the input is not between 1 and (20 - original amount), we create error messages representing what the user 
did wrong.
'''

def restock_comic():
    for i in comics:
        try:
            if restock_name.get() == i._name:
                if int(restock_amount.get()) >= 1 and (int(restock_amount.get()) + i._amount) <= 20:
                    i.restock(int(restock_amount.get()))
                    restock_error_msg.set("Successfully restocked {} {} comic(s)".format(int(restock_amount.get()), i._name))

                elif int(restock_amount.get()) < 1:
                    restock_error_msg.set("Please enter a value that is larger than 0!")

                elif (int(restock_amount.get()) + i._amount) > 20:
                    restock_error_msg.set("You can only have maximum 20 comics!")

        except ValueError:
            restock_error_msg.set("Please enter an integer value!")

    update_label()

#Create delete_comic() function
def delete_comic():
    if messagebox.askyesno("Delete this Comic?", "Are you sure you want to delete " + delete_name.get() + "? "):
        #Loop through comics
        for i in comics:
            #If the looped name is equal to the desired name from use
            if delete_name.get() == i._name:
                #Remove the comic from both comics and comic_names list
                comics.remove(i)
                comic_names.remove(i._name)
                update_label()
                update_menus()

#Create class called Comics
class Comics:
    #Initial initial function
    def __init__(self, name, amount, sold):
        self._name = name 
        self._amount = amount
        self._sold = sold
        #Append the comic and its name to comics and comic_names list
        comics.append(self)
        comic_names.append(self._name)

    #Create function for restocking
    def restock(self, amount):
        self._amount += amount

    #Create function for selling (minus amount)
    def sell_comic(self, amount):
        self._amount -= amount

    #Create function for selling (add amount sold)
    def sell_number(self, amount):
        self._sold += amount
        
    

#Initial comics and comic_names list
comics = []
comic_names = []

#Initiate 3 comics for each comic
Comics("Python Panic", 8, 0)
Comics("Scratch the Cat", 12, 0)
Comics("Tony Tkinter", 3, 0)

#Initialise tkinter window
root = Tk()
root.title("comics label")
root.geometry('800x1000')

#Set up frames for showing information, adding window, restock window and delete window 
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

'''
Selling Window
'''

#Set up comic_info() stringVar
comic_info = StringVar()

#Set up comic label using comic_info
comic_lbl = Label(info_frame, textvariable=comic_info)
comic_lbl.grid(row = 0, columnspan = 2)

#Set up label showing "Selling Window"
selling_window = Label(info_frame, text = "Selling Window")
selling_window.grid(row = 1, columnspan = 2)

#Set up quantity sold label
quantity_sold = Label(info_frame, text = "Quantity Sold")
quantity_sold.grid(row = 2, column = 0)

#Set up selected_comic stringVar and default it to comic_names[0]
selected_comic = StringVar()
selected_comic.set(comic_names[0])

#Set up comic_menu optionmenu using comic_names
comic_menu = OptionMenu(info_frame, selected_comic, *comic_names)
comic_menu.grid(row = 2, column = 0)

#Set up num_comics StringVar
num_comics = StringVar()

#Set up comic_entry using num_comics
comic_entry = Entry(info_frame, textvariable=num_comics)
comic_entry.grid(row = 2, column = 1)

#Set up button linked to change_sold function
select_btn = Button(info_frame, text="Select", command=change_sold)
select_btn.grid(row = 3, columnspan = 2)

#Set up error message
error_msg = StringVar()
error_msg.set("")

#Set up error label
selling_error = Label(info_frame, textvariable=error_msg)
selling_error.grid(row= 4, columnspan = 2)

'''
Add Window
'''

#Set up label which says "Adding Window"
add_window = Label(add_frame, text="Adding Window")
add_window.grid(row = 0, columnspan = 2)

#Set up name_lbl 
name_lbl = Label(add_frame, text = "Name ")
name_lbl.grid(row = 1, column = 0)

#Set up add_name StringVar
add_name = StringVar()

#Set up add_entry
add_entry = Entry(add_frame, textvariable=add_name)
add_entry.grid(row = 1, column = 1)

#Set up amount_lbl
amount_lbl = Label(add_frame, text = "Quantity ")
amount_lbl.grid(row = 2, column = 0)

#Set up add_amount StringVar
add_amount = StringVar()

#Set up amount_entry linked to add_amount
amount_entry = Entry(add_frame, textvariable=add_amount)
amount_entry.grid(row = 2, column = 1)

#Set up add_btn
add_btn = Button(add_frame, text="Select", command=add_comic)
add_btn.grid(row = 3, columnspan = 2)

#Set up add_error_msg
add_error_msg = StringVar()
add_error_msg.set("")

#Set up add_error
add_error = Label(add_frame, textvariable=add_error_msg)
add_error.grid(row= 4 , columnspan = 2)

'''Restock Window'''

#Set up restock_window showing text "Restock Window"
restock_window = Label(restock_frame, text="Restock Window")
restock_window.grid(row = 0, columnspan = 2)

#Set up restock_name_lbl
restock_name_lbl = Label(restock_frame, text = "Name ")
restock_name_lbl.grid(row = 1, column = 0)

#Set up restock_name
restock_name = StringVar()
restock_name.set(comic_names[0])

#Set up restock_option
restock_option = OptionMenu(restock_frame, restock_name, *comic_names)
restock_option.grid(row = 1, column = 1)

#Set up restock_amount_lbl
restock_amount_lbl = Label(restock_frame, text = "Quantity ")
restock_amount_lbl.grid(row = 2, column = 0)

#Set up restock_amount
restock_amount = StringVar()

#Set up restock_amount_entry
restock_amount_entry = Entry(restock_frame, textvariable=restock_amount)
restock_amount_entry.grid(row = 2, column = 1)

#Set up restock_btn linked to restock_comic function
restock_btn = Button(restock_frame, text="Select", command=restock_comic)
restock_btn.grid(row = 3, columnspan = 2)

#Set up restock_error_msg StringVar
restock_error_msg = StringVar()
restock_error_msg.set("")

#Set up restock_error using restock_error_msg
restock_error = Label(restock_frame, textvariable=restock_error_msg)
restock_error.grid(row= 4 , columnspan = 2)

'''Delete Stock'''

#Set up delete_window label showing "Delete Window"
delete_window = Label(delete_frame, text="Delete Window")
delete_window.grid(row = 0, columnspan = 2)

#Set up delete_name_lbl
delete_name_lbl = Label(delete_frame, text = "Name ")
delete_name_lbl.grid(row = 1, column = 0)

#Set up delete_name
delete_name = StringVar()
delete_name.set(comic_names[0])

#Set up delete_option option menu using comic_names
delete_option = OptionMenu(delete_frame, delete_name, *comic_names)
delete_option.grid(row = 1, column = 1)

#Set up delete_btn connected to delete_comic function
delete_btn = Button(delete_frame, text="Select", command=delete_comic)
delete_btn.grid(row = 3, columnspan = 2)

#Set up delete_error_msg
delete_error_msg = StringVar()
delete_error_msg.set("")

#Set up delete_error
delete_error = Label(delete_frame, textvariable=delete_error_msg)
delete_error.grid(row= 4 , columnspan = 2)

#Run update_label function
update_label()
#Initialise mainloop() for root
root.mainloop()