from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from ttkbootstrap import *

ablak=Tk()
ablak.resizable(False, False)
ablak.title("Mozifalva")
ablak.geometry("800x800")
ablak.configure(bg="#2a1a1d")
logo = PhotoImage(file="Mozifalva.png")
kep = Label(ablak, image=logo)
kep.place(x=400, y=200, anchor=CENTER)
fogomb = Button(ablak, bootstyle="dark", text="Belépés", width=30)
fogomb.place(x=400, y=700, anchor=CENTER)







ablak.mainloop()