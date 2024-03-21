from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from ttkbootstrap import *



ablak=Window(themename="vapor")
ablak.resizable(False, False)
ablak.title("Mozifalva")
ablak.geometry("800x800")
ablak.configure(background="black")
logo = PhotoImage(file="popcorntownfinal.png")
kep = Label(ablak, image=logo , borderwidth=0)
kep.place(x=400, y=300, anchor=CENTER)
mystyle=Style()
mystyle.configure("danger.TButton")
fogomb = Button(ablak, bootstyle="danger", style="danger.TButton", text="BELÉPÉS", width=30)
fogomb.place(x=400, y=700, anchor=CENTER)







ablak.mainloop()