from tkinter import *

#def update_label():
    #ticket_info.set("")
    #for p in tickets:
        #ticket_info.set(ticket_info.get() + p._name + " $" + str(p._price) + " " + str(p._amount) + "\n")

root = Tk()
root.title("Tickets label")
root.geometry('800x1000')

frame1 = Frame(root, relief = "groove", borderwidth = 2, width = 800).grid(row = 0, column = 0, sticky = N+S+W+E)
frame2 = Frame(root, relief = "groove", borderwidth = 2, width = 400).grid(row = 1, column = 0, sticky = N+S+W+E)
frame3 = Frame(root, relief = "groove", borderwidth = 2, width = 400).grid(row = 1, column = 1, sticky = N+S+W+E)
frame4 = Frame(root, relief = "groove", borderwidth = 2, width = 400).grid(row = 2, column = 0, sticky = N+S+W+E)
frame5 = Frame(root, relief = "groove", borderwidth = 2, width = 400).grid(row = 2, column = 1, sticky = N+S+W+E)


ticket_info = StringVar()

ticket_lbl = Label(root, textvariable=ticket_info)
ticket_lbl.grid(row=0)

#update_label()
root.mainloop()