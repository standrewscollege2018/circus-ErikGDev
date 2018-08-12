from tkinter import *

def update_label():
    ticket_info.set("")
    for p in tickets:
        ticket_info.set(ticket_info.get() + p._name + " $" + str(p._price) + " " + str(p._amount) + "\n")

def change_stuff():
    for i in tickets:
        if selected_ticket.get() == i._name:
            i._amount -= int(num_tickets.get())
            tickets_sold.set(int(tickets_sold.get()) + int(num_tickets.get()))
        print(i._name)
        print(i._price)

    update_label()

class Tickets:
    def __init__(self, name, price, amount):
        self._name = name 
        self._price = price
        self._amount = amount
        tickets.append(self)
        ticket_names.append(self._name)

tickets = []
ticket_names = []

Tickets("10am", 5, 150)
Tickets("3pm", 5, 150)
Tickets("8pm", 12, 250)

root = Tk()
root.title("Tickets label")
root.geometry('500x500')

ticket_info = StringVar()

ticket_lbl = Label(root, textvariable=ticket_info)
ticket_lbl.grid(row=0)

selected_ticket = StringVar()
selected_ticket.set(ticket_names[0])

ticket_menu = OptionMenu(root, selected_ticket, *ticket_names)
ticket_menu.grid(row=1)

num_tickets = StringVar()

ticket_entry = Entry(root, textvariable=num_tickets)
ticket_entry.grid(row=2)

select_btn = Button(root, text="Select", command=change_stuff)
select_btn.grid(row=3)

tickets_sold = StringVar()
tickets_sold.set(0)

sold_lbl = Label(root, textvariable = tickets_sold)
sold_lbl.grid(row=4)

tickets_total = StringVar()
tickets_total.set("$0")

dollar_lbl = Label(root, textvariable = tickets_total)
dollar_lbl.grid(row=5)

update_label()
root.mainloop()