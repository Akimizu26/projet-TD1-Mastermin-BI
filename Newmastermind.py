from tkinter import Label, Tk
from tkinter.ttk import Combobox

root = Tk()
root.title("Mastermind TD01")
root.config(bg='blue')

Label(root, text='Choisissez un nombre:').pack()
my_box = Combobox(root, values=(2, 4, 6, 8))
my_box.current(2)
my_box.pack()

root.mainloop()
