from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from ttkbootstrap import *


def belepes():
    topk=Toplevel()
    topk.iconbitmap("kiskep.ico")
    topk.geometry("800x800")
    topk.title("Filmek")
    topk.configure(background="black")
    filmektabla=Label(topk, text="Választható filmek:", foreground="red", font=('Ariel', 20), background="black") 
    filmektabla.place(x=400, y=100, anchor=CENTER)
    dunekep = PhotoImage(file="dune2.png")
    dunelabel = Label(topk, image=dunekep , borderwidth=0)
    dunelabel.place(x=400, y=300, anchor=CENTER)
    


ablak=Window(themename="vapor")
ablak.iconbitmap("kiskep.ico")
ablak.resizable(False, False)
ablak.title("Mozifalva")
ablak.geometry("800x800")
ablak.configure(background="black")
logo = PhotoImage(file="popcorntownfinal.png")
kep = Label(ablak, image=logo , borderwidth=0)
kep.place(x=400, y=300, anchor=CENTER)
mystyle=Style()
mystyle.configure("danger.TButton")
fogomb = Button(ablak, bootstyle="danger", style="danger.TButton", text="BELÉPÉS", width=30, command=belepes)
fogomb.place(x=400, y=700, anchor=CENTER)



ablak.mainloop()