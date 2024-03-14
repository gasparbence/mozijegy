from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from ttkbootstrap import *
from PIL import Image


ablak=Window(themename='lumen')
ablak.resizable(False, False)
ablak.title("Mozifalva")
ablak.geometry("800x800")
ablak.configure(background="#2a1a1d")
logo = PhotoImage(file="Mozifalva.png")
kep = Label(ablak, image=logo)
kep.place(x=400, y=300, anchor=CENTER)
mystyle=Style()
mystyle.configure("dark.Outline.TButton")
fogomb = Button(ablak, bootstyle="dark", style="dark.Outline.TButton", text="BELÉPÉS", width=30)
fogomb.place(x=400, y=700, anchor=CENTER)







ablak.mainloop()