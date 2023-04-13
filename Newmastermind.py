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
label (root, text='Jeu du mastermind').pack(fill='x')
Button (root, text='Bouton start').pack(fill='x',expand=True) 
Button (root, text='bouton setting').pack(fill='y',expand=True)
Button (root, text='Bouton sortie').pack(fill='both',expand=True)

root.mainloop()
