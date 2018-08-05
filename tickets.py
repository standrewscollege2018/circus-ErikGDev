from tkinter import *

def update_label():
    ticket_info.set("")
    for p in tickets:
        ticket_info.set(ticket_info.get() + p._name + " $" + str(p._price))

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
selected_ticket.set(tickets[0])


update_label()
root.mainloop()