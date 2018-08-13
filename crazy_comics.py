from tkinter import *

def update_label():
    comic_info.set("")
    for p in comics:
        comic_info.set(comic_info.get() + p._name + " $" + str(p._price) + " " + str(p._amount) + "\n")

class Comics:
    def __init__(self, name, amount):
        self._name = name 
        self._amount = amount
        comics.append(self)
        comic_names.append(self._name)

comics = []
comic_names = []



root = Tk()
root.title("comics label")
root.geometry('800x1000')

frame1 = Frame(root, relief = "groove", borderwidth = 2, width = 800).grid(row = 0, column = 0, sticky = N+S+W+E)
frame2 = Frame(root, relief = "groove", borderwidth = 2, width = 400).grid(row = 1, column = 0, sticky = N+S+W+E)
frame3 = Frame(root, relief = "groove", borderwidth = 2, width = 400).grid(row = 1, column = 1, sticky = N+S+W+E)
frame4 = Frame(root, relief = "groove", borderwidth = 2, width = 400).grid(row = 2, column = 0, sticky = N+S+W+E)
frame5 = Frame(root, relief = "groove", borderwidth = 2, width = 400).grid(row = 2, column = 1, sticky = N+S+W+E)



comic_info = StringVar()

comic_lbl = Label(frame1, textvariable=comic_info)
comic_lbl.grid(row=0)

update_label()
root.mainloop()