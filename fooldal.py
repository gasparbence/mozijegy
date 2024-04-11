from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from ttkbootstrap import *


def belepes():
    topk=Toplevel()
    topk.iconbitmap("kiskep.ico")
    topk.geometry("1300x650")
    topk.title("Filmek")
    topk.configure(background="black")
    filmektabla=Label(topk, text="Választható filmek:", foreground="red", font=('Ariel', 20), background="black") 
    filmektabla.place(x=650, y=100, anchor=CENTER)
    
    dunekep = PhotoImage(file="J:\IKT\Mozijegyfoglalo\mozijegy\dune2.png")
    dunelabel = Label(topk, image=dunekep , borderwidth=0)
    dunelabel.place(x=650, y=300, anchor=CENTER)
    oppenheimerkep = PhotoImage(file="J:\IKT\Mozijegyfoglalo\mozijegy\oppenheimer.png")
    oppenheimerlabel = Label(topk, image=oppenheimerkep , borderwidth=0)
    oppenheimerlabel.place(x=150, y=300, anchor=CENTER)
    mostkep = PhotoImage(file="J:\IKT\Mozijegyfoglalo\mozijegy\mostvagysoha.png")
    mostlabel = Label(topk, image=mostkep , borderwidth=0)
    mostlabel.place(x=400, y=300, anchor=CENTER)
    
    dunereszletek = Button(topk, bootstyle="danger", style="danger.TButton", text="RÉSZLETEK", width=30)
    dunereszletek.place(x=650, y=500, anchor=CENTER)
    oppenheimerreszletek = Button(topk, bootstyle="danger", style="danger.TButton", text="RÉSZLETEK", width=30)
    oppenheimerreszletek.place(x=150, y=500, anchor=CENTER)
    mostreszletek = Button(topk, bootstyle="danger", style="danger.TButton", text="RÉSZLETEK", width=30)
    mostreszletek.place(x=400, y=500, anchor=CENTER)
    meheszreszletek = Button(topk, bootstyle="danger", style="danger.TButton", text="RÉSZLETEK", width=30)
    meheszreszletek.place(x=900, y=500, anchor=CENTER)
    godzillareszletek = Button(topk, bootstyle="danger", style="danger.TButton", text="RÉSZLETEK", width=30)
    godzillareszletek.place(x=1150, y=500, anchor=CENTER)
    
    dunefoglalas = Button(topk, bootstyle="danger", style="danger.TButton", text="FOGLALÁS", width=30)
    dunefoglalas.place(x=650, y=540, anchor=CENTER)
    oppenheimerfoglalas = Button(topk, bootstyle="danger", style="danger.TButton", text="FOGLALÁS", width=30)
    oppenheimerfoglalas.place(x=150, y=540, anchor=CENTER)
    mostfoglalas = Button(topk, bootstyle="danger", style="danger.TButton", text="FOGLALÁS", width=30)
    mostfoglalas.place(x=400, y=540, anchor=CENTER)
    meheszfoglalas = Button(topk, bootstyle="danger", style="danger.TButton", text="FOGLALÁS", width=30)
    meheszfoglalas.place(x=900, y=540, anchor=CENTER)
    godzillafoglalas = Button(topk, bootstyle="danger", style="danger.TButton", text="FOGLALÁS", width=30)
    godzillafoglalas.place(x=1150, y=540, anchor=CENTER)
    
    error = Button(topk, bootstyle="danger", style="danger.TButton", text="FOGLALÁS", width=15)
    error.place(x=750, y=750, anchor=LEFT)
    


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