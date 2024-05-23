from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from ttkbootstrap import *

def visszaoppen():
    global topoppen
    topoppen.destroy()

def visszamost():
    global topmost
    topmost.destroy()

def visszadune():
    global topdune
    topdune.destroy()

def visszamehesz():
    global topmehesz
    topmehesz.destroy()

def visszagk():
    global topgk
    topgk.destroy()
    
def visszafoglal():
    global foglalablak
    foglalablak.destroy()

def megrendelfoglal():
    global foglalablak, neventry, emailentry
    nev = neventry.get()
    email = emailentry.get()
    print(nev, email)
    

def resetfoglal():
    global foglalablak, neventry, emailentry, szek11, szek12, szek13, szek14, szek15, szek16, szek17, szek18, szek19, szek21, szek22, szek23, szek24, szek25, szek26, szek27, szek28, szek29, szek31, szek32, szek33, szek34, szek35, szek36, szek37, szek38, szek39, szek41, szek42, szek43, szek44, szek45, szek46, szek47, szek48, szek49, szek51, szek52, szek53, szek54, szek55, szek56, szek57, szek58, szek59, szek61, szek62, szek63, szek64, szek65, szek66, szek67, szek68, szek69, szek610
    emailentry.configure(textvariable=" ")
    neventry.configure(textvariable="  ")
    szek11.configure(bootstyle="danger")
    szek12.configure(bootstyle="danger")
    szek13.configure(bootstyle="danger")
    szek14.configure(bootstyle="danger")
    szek15.configure(bootstyle="danger")
    szek16.configure(bootstyle="danger")
    szek17.configure(bootstyle="danger")
    szek18.configure(bootstyle="danger")
    szek19.configure(bootstyle="danger")
    szek21.configure(bootstyle="danger")
    szek22.configure(bootstyle="danger")
    szek23.configure(bootstyle="danger")
    szek24.configure(bootstyle="danger")
    szek25.configure(bootstyle="danger")
    szek26.configure(bootstyle="danger")
    szek27.configure(bootstyle="danger")
    szek28.configure(bootstyle="danger")
    szek29.configure(bootstyle="danger")
    szek31.configure(bootstyle="danger")
    szek32.configure(bootstyle="danger")
    szek33.configure(bootstyle="danger")
    szek34.configure(bootstyle="danger")
    szek35.configure(bootstyle="danger")
    szek36.configure(bootstyle="danger")
    szek37.configure(bootstyle="danger")
    szek38.configure(bootstyle="danger")
    szek39.configure(bootstyle="danger")
    szek41.configure(bootstyle="danger")
    szek42.configure(bootstyle="danger")
    szek43.configure(bootstyle="danger")
    szek44.configure(bootstyle="danger")
    szek45.configure(bootstyle="danger")
    szek46.configure(bootstyle="danger")
    szek47.configure(bootstyle="danger")
    szek48.configure(bootstyle="danger")
    szek49.configure(bootstyle="danger")
    szek51.configure(bootstyle="danger")
    szek52.configure(bootstyle="danger")
    szek53.configure(bootstyle="danger")
    szek54.configure(bootstyle="danger")
    szek55.configure(bootstyle="danger")
    szek56.configure(bootstyle="danger")
    szek57.configure(bootstyle="danger")
    szek58.configure(bootstyle="danger")
    szek59.configure(bootstyle="danger")
    szek61.configure(bootstyle="danger")
    szek62.configure(bootstyle="danger")
    szek63.configure(bootstyle="danger")
    szek64.configure(bootstyle="danger")
    szek65.configure(bootstyle="danger")
    szek66.configure(bootstyle="danger")
    szek67.configure(bootstyle="danger")
    szek68.configure(bootstyle="danger")
    szek69.configure(bootstyle="danger")
    szek610.configure(bootstyle="danger")
    
    
    
def gomb11():
    global szek11, ertek
    ertek -= 1
    if ertek == 0:
        szek11.configure(bootstyle="success")
        ertek = 1
def gomb12():
    global szek12, ertek
    ertek -= 1
    if ertek == 0:
        szek12.configure(bootstyle="success")
        ertek = 1
def gomb13():
    global szek13, ertek
    ertek -= 1
    if ertek == 0:
        szek13.configure(bootstyle="success")
        ertek = 1
def gomb14():
    global szek14, ertek
    ertek -= 1
    if ertek == 0:
        szek14.configure(bootstyle="success")
        ertek = 1
def gomb15():
    global szek15, ertek
    ertek -= 1
    if ertek == 0:
        szek15.configure(bootstyle="success")
        ertek = 1
def gomb16():
    global szek16, ertek
    ertek -= 1
    if ertek == 0:
        szek16.configure(bootstyle="success")
        ertek = 1
def gomb17():
    global szek17, ertek
    ertek -= 1
    if ertek == 0:
        szek17.configure(bootstyle="success")
        ertek = 1
def gomb18():
    global szek18, ertek
    ertek -= 1
    if ertek == 0:
        szek18.configure(bootstyle="success")
        ertek = 1
def gomb19():
    global szek19, ertek
    ertek -= 1
    if ertek == 0:
        szek19.configure(bootstyle="success")
        ertek = 1
def gomb21():
    global szek21, ertek
    ertek -= 1
    if ertek == 0:
        szek21.configure(bootstyle="success")
        ertek = 1
def gomb22():
    global szek22, ertek
    ertek -= 1
    if ertek == 0:
        szek22.configure(bootstyle="success")
        ertek = 1
def gomb23():
    global szek23, ertek
    ertek -= 1
    if ertek == 0:
        szek23.configure(bootstyle="success")
        ertek = 1
def gomb24():
    global szek24, ertek
    ertek -= 1
    if ertek == 0:
        szek24.configure(bootstyle="success")
        ertek = 1
def gomb25():
    global szek25, ertek
    ertek -= 1
    if ertek == 0:
        szek25.configure(bootstyle="success")
        ertek = 1
def gomb26():
    global szek26, ertek
    ertek -= 1
    if ertek == 0:
        szek26.configure(bootstyle="success")
        ertek = 1
def gomb27():
    global szek27, ertek
    ertek -= 1
    if ertek == 0:
        szek27.configure(bootstyle="success")
        ertek = 1
def gomb28():
    global szek28, ertek
    ertek -= 1
    if ertek == 0:
        szek28.configure(bootstyle="success")
        ertek = 1
def gomb29():
    global szek29, ertek
    ertek -= 1
    if ertek == 0:
        szek29.configure(bootstyle="success")
        ertek = 1
def gomb31():
    global szek31, ertek
    ertek -= 1
    if ertek == 0:
        szek31.configure(bootstyle="success")
        ertek = 1
def gomb32():
    global szek32, ertek
    ertek -= 1
    if ertek == 0:
        szek32.configure(bootstyle="success")
        ertek = 1
def gomb33():
    global szek33, ertek
    ertek -= 1
    if ertek == 0:
        szek33.configure(bootstyle="success")
        ertek = 1
def gomb34():
    global szek34, ertek
    ertek -= 1
    if ertek == 0:
        szek34.configure(bootstyle="success")
        ertek = 1
def gomb35():
    global szek35, ertek
    ertek -= 1
    if ertek == 0:
        szek35.configure(bootstyle="success")
        ertek = 1
def gomb36():
    global szek36, ertek
    ertek -= 1
    if ertek == 0:
        szek36.configure(bootstyle="success")
        ertek = 1
def gomb37():
    global szek37, ertek
    ertek -= 1
    if ertek == 0:
        szek37.configure(bootstyle="success")
        ertek = 1
def gomb38():
    global szek38, ertek
    ertek -= 1
    if ertek == 0:
        szek38.configure(bootstyle="success")
        ertek = 1
def gomb39():
    global szek39, ertek
    ertek -= 1
    if ertek == 0:
        szek39.configure(bootstyle="success")
        ertek = 1
def gomb41():
    global szek41, ertek
    ertek -= 1
    if ertek == 0:
        szek41.configure(bootstyle="success")
        ertek = 1
def gomb42():
    global szek42, ertek
    ertek -= 1
    if ertek == 0:
        szek42.configure(bootstyle="success")
        ertek = 1
def gomb43():
    global szek43, ertek
    ertek -= 1
    if ertek == 0:
        szek43.configure(bootstyle="success")
        ertek = 1
def gomb44():
    global szek44, ertek
    ertek -= 1
    if ertek == 0:
        szek44.configure(bootstyle="success")
        ertek = 1
def gomb45():
    global szek45, ertek
    ertek -= 1
    if ertek == 0:
        szek45.configure(bootstyle="success")
        ertek = 1
def gomb46():
    global szek46, ertek
    ertek -= 1
    if ertek == 0:
        szek46.configure(bootstyle="success")
        ertek = 1
def gomb47():
    global szek47, ertek
    ertek -= 1
    if ertek == 0:
        szek47.configure(bootstyle="success")
        ertek = 1
def gomb48():
    global szek48, ertek
    ertek -= 1
    if ertek == 0:
        szek48.configure(bootstyle="success")
        ertek = 1
def gomb49():
    global szek49, ertek
    ertek -= 1
    if ertek == 0:
        szek49.configure(bootstyle="success")
        ertek = 1
def gomb51():
    global szek51, ertek
    ertek -= 1
    if ertek == 0:
        szek51.configure(bootstyle="success")
        ertek = 1
def gomb52():
    global szek52, ertek
    ertek -= 1
    if ertek == 0:
        szek52.configure(bootstyle="success")
        ertek = 1
def gomb53():
    global szek53, ertek
    ertek -= 1
    if ertek == 0:
        szek53.configure(bootstyle="success")
        ertek = 1
def gomb54():
    global szek54, ertek
    ertek -= 1
    if ertek == 0:
        szek54.configure(bootstyle="success")
        ertek = 1
def gomb55():
    global szek55, ertek
    ertek -= 1
    if ertek == 0:
        szek55.configure(bootstyle="success")
        ertek = 1
def gomb56():
    global szek56, ertek
    ertek -= 1
    if ertek == 0:
        szek56.configure(bootstyle="success")
        ertek = 1
def gomb57():
    global szek57, ertek
    ertek -= 1
    if ertek == 0:
        szek57.configure(bootstyle="success")
        ertek = 1
def gomb58():
    global szek58, ertek
    ertek -= 1
    if ertek == 0:
        szek58.configure(bootstyle="success")
        ertek = 1
def gomb59():
    global szek59, ertek
    ertek -= 1
    if ertek == 0:
        szek59.configure(bootstyle="success")
        ertek = 1
def gomb61():
    global szek61, ertek
    ertek -= 1
    if ertek == 0:
        szek61.configure(bootstyle="success")
        ertek = 1
def gomb62():
    global szek62, ertek
    ertek -= 1
    if ertek == 0:
        szek62.configure(bootstyle="success")
        ertek = 1
def gomb63():
    global szek63, ertek
    ertek -= 1
    if ertek == 0:
        szek63.configure(bootstyle="success")
        ertek = 1
def gomb64():
    global szek64, ertek
    ertek -= 1
    if ertek == 0:
        szek64.configure(bootstyle="success")
        ertek = 1
def gomb65():
    global szek65, ertek
    ertek -= 1
    if ertek == 0:
        szek65.configure(bootstyle="success")
        ertek = 1
def gomb66():
    global szek66, ertek
    ertek -= 1
    if ertek == 0:
        szek66.configure(bootstyle="success")
        ertek = 1
def gomb67():
    global szek67, ertek
    ertek -= 1
    if ertek == 0:
        szek67.configure(bootstyle="success")
        ertek = 1
def gomb68():
    global szek68, ertek
    ertek -= 1
    if ertek == 0:
        szek68.configure(bootstyle="success")
        ertek = 1
def gomb69():
    global szek69, ertek
    ertek -= 1
    if ertek == 0:
        szek69.configure(bootstyle="success")
        ertek = 1
def gomb610():
    global szek610, ertek
    ertek -= 1
    if ertek == 0:
        szek610.configure(bootstyle="success")
        ertek = 1

def foglalas():
    global foglalablak, kiskep, neventry, emailentry, szek11, szek12, szek13, szek14, szek15, szek16, szek17, szek18, szek19, szek21, szek22, szek23, szek24, szek25, szek26, szek27, szek28, szek29, szek31, szek32, szek33, szek34, szek35, szek36, szek37, szek38, szek39, szek41, szek42, szek43, szek44, szek45, szek46, szek47, szek48, szek49, szek51, szek52, szek53, szek54, szek55, szek56, szek57, szek58, szek59, szek61, szek62, szek63, szek64, szek65, szek66, szek67, szek68, szek69, szek610, ertek
    ertek = 1
    foglalablak=Toplevel()
    foglalablak.iconbitmap("J:\IKT\Mozijegyfoglalo\kiskep.ico")
    foglalablak.geometry("1300x650")
    foglalablak.title("Foglalás")
    foglalablak.resizable(False, False)
    foglalablak.configure(background="black")
    kiskep2 = Image.open("J:\IKT\Mozijegyfoglalo\mozijegy\popcorntownfinalkicsi.png")
    kiskep2 = ImageTk.PhotoImage(kiskep2)
    image_label = Label(foglalablak, image=kiskep) 
    image_label.place(x=1210, y=70, anchor=CENTER)
    foglalcim = Label(foglalablak, text="Székek foglalása:", font=("Ariel", 20), foreground="#e34b54", background="black")
    foglalcim.place(x=600, y=100)
    megrendel = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="MEGRENDEL", width=30, command=megrendelfoglal)
    megrendel.place(x=1025, y=450, anchor=CENTER)
    foglalvissza = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="VISSZA", width=30, command=visszafoglal)
    foglalvissza.place(x=900, y=500, anchor=CENTER)
    reset = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="RESET", width=30, command=resetfoglal)
    reset.place(x=1150, y=500, anchor=CENTER)
    emaillabel = Label(foglalablak, text="E-mail: ", font=("Ariel", 15), foreground="#e34b54", background="black")
    emaillabel.place(x=800, y=350)
    emailentry = Entry(foglalablak, font=("Ariel", 10), width=50, bootstyle="danger")
    emailentry.place(x=880, y=350)
    nevlabel = Label(foglalablak, text="Név: ", font=("Ariel", 15), foreground="#e34b54", background="black")
    nevlabel.place(x=800, y=300)
    neventry = Entry(foglalablak, font=("Ariel", 10), width=50, bootstyle="danger")
    neventry.place(x=880, y=300)
    rendadatoklabel = Label(foglalablak, text="Rendelés adatai: ", font=("Ariel", 18), foreground="#e34b54", background="black")
    rendadatoklabel.place(x=925, y=250)

    sorszam1 = Label(foglalablak, text="1. sor:", font=("Ariel", 15), foreground="#e34b54", background="black")
    sorszam1.place(x=180, y=200)
    szek11 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="1", width=3, command=gomb11)
    szek11.place(x=250, y=200)
    szek12 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="2", width=3, command=gomb12)
    szek12.place(x=300, y=200)
    szek13 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="3", width=3, command=gomb13)
    szek13.place(x=350, y=200)
    szek14 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="4", width=3, command=gomb14)
    szek14.place(x=400, y=200)
    szek15 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="5", width=3, command=gomb15)
    szek15.place(x=500, y=200)
    szek16 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="6", width=3, command=gomb16)
    szek16.place(x=550, y=200)
    szek17 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="7", width=3, command=gomb17)
    szek17.place(x=600, y=200)
    szek18 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="8", width=3, command=gomb18)
    szek18.place(x=650, y=200)
    szek19 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="9", width=3, command=gomb19)
    szek19.place(x=700, y=200)
    
    sorszam2 = Label(foglalablak, text="2. sor:", font=("Ariel", 15), foreground="#e34b54", background="black")
    sorszam2.place(x=180, y=240)
    szek21 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="1", width=3, command=gomb21)
    szek21.place(x=250, y=240)
    szek22 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="2", width=3, command=gomb22)
    szek22.place(x=300, y=240)
    szek23 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="3", width=3, command=gomb23)
    szek23.place(x=350, y=240)
    szek24 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="4", width=3, command=gomb24)
    szek24.place(x=400, y=240)
    szek25 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="5", width=3, command=gomb25)
    szek25.place(x=500, y=240)
    szek26 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="6", width=3, command=gomb26)
    szek26.place(x=550, y=240)
    szek27 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="7", width=3, command=gomb27)
    szek27.place(x=600, y=240)
    szek28 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="8", width=3, command=gomb28)
    szek28.place(x=650, y=240)
    szek29 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="9", width=3, command=gomb29)
    szek29.place(x=700, y=240)
    
    sorszam3 = Label(foglalablak, text="3. sor:", font=("Ariel", 15), foreground="#e34b54", background="black")
    sorszam3.place(x=180, y=280)
    szek31 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="1", width=3, command=gomb31)
    szek31.place(x=250, y=280)
    szek32 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="2", width=3, command=gomb32)
    szek32.place(x=300, y=280)
    szek33 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="3", width=3, command=gomb33)
    szek33.place(x=350, y=280)
    szek34 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="4", width=3, command=gomb34)
    szek34.place(x=400, y=280)
    szek35 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="5", width=3, command=gomb35)
    szek35.place(x=500, y=280)
    szek36 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="6", width=3, command=gomb36)
    szek36.place(x=550, y=280)
    szek37 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="7", width=3, command=gomb37)
    szek37.place(x=600, y=280)
    szek38 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="8", width=3, command=gomb38)
    szek38.place(x=650, y=280)
    szek39 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="9", width=3, command=gomb39)
    szek39.place(x=700, y=280)
    
    sorszam4 = Label(foglalablak, text="4. sor:", font=("Ariel", 15), foreground="#e34b54", background="black")
    sorszam4.place(x=180, y=320)
    szek41 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="1", width=3, command=gomb41)
    szek41.place(x=250, y=320)
    szek42 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="2", width=3, command=gomb42)
    szek42.place(x=300, y=320)
    szek43 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="3", width=3, command=gomb43)
    szek43.place(x=350, y=320)
    szek44 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="4", width=3, command=gomb44)
    szek44.place(x=400, y=320)
    szek45 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="5", width=3, command=gomb45)
    szek45.place(x=500, y=320)
    szek46 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="6", width=3, command=gomb46)
    szek46.place(x=550, y=320)
    szek47 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="7", width=3, command=gomb47)
    szek47.place(x=600, y=320)
    szek48 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="8", width=3, command=gomb48)
    szek48.place(x=650, y=320)
    szek49 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="9", width=3, command=gomb49)
    szek49.place(x=700, y=320)
    
    sorszam5 = Label(foglalablak, text="5. sor:", font=("Ariel", 15), foreground="#e34b54", background="black")
    sorszam5.place(x=180, y=360)
    szek51 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="1", width=3, command=gomb51)
    szek51.place(x=250, y=360)
    szek52 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="2", width=3, command=gomb52)
    szek52.place(x=300, y=360)
    szek53 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="3", width=3, command=gomb53)
    szek53.place(x=350, y=360)
    szek54 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="4", width=3, command=gomb54)
    szek54.place(x=400, y=360)
    szek55 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="5", width=3, command=gomb55)
    szek55.place(x=500, y=360)
    szek56 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="6", width=3, command=gomb56)
    szek56.place(x=550, y=360)
    szek57 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="7", width=3, command=gomb57)
    szek57.place(x=600, y=360)
    szek58 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="8", width=3, command=gomb58)
    szek58.place(x=650, y=360)
    szek59 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="9", width=3, command=gomb59)
    szek59.place(x=700, y=360)
    
    sorszam6 = Label(foglalablak, text="6. sor:", font=("Ariel", 15), foreground="#e34b54", background="black")
    sorszam6.place(x=180, y=400)
    szek61 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="1", width=3, command=gomb61)
    szek61.place(x=250, y=400)
    szek62 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="2", width=3, command=gomb62)
    szek62.place(x=300, y=400)
    szek63 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="3", width=3, command=gomb63)
    szek63.place(x=350, y=400)
    szek64 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="4", width=3, command=gomb64)
    szek64.place(x=400, y=400)
    szek65 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="5", width=3, command=gomb65)
    szek65.place(x=450, y=400)
    szek66 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="6", width=3, command=gomb66)
    szek66.place(x=500, y=400)
    szek67 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="7", width=3, command=gomb67)
    szek67.place(x=550, y=400)
    szek68 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="8", width=3, command=gomb68)
    szek68.place(x=600, y=400)
    szek69 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="9", width=3, command=gomb69)
    szek69.place(x=650, y=400)
    szek610 = Button(foglalablak, bootstyle="danger", style="danger.TButton", text="10", width=3, command=gomb610)
    szek610.place(x=700, y=400)
    
    
    
    


def reszletekoppen():
    global oppenheimerkep2, topoppen
    topoppen=Toplevel()
    topoppen.iconbitmap("J:\IKT\Mozijegyfoglalo\kiskep.ico")
    topoppen.geometry("1300x650")
    topoppen.title("Részletek")
    topoppen.resizable(False, False)
    topoppen.configure(background="black")
    oppenheimerkep2 = PhotoImage(file="J:\IKT\Mozijegyfoglalo\mozijegy\oppenheimernagy.png")
    oppenheimerlabel = Label(topoppen, image=oppenheimerkep2, borderwidth=0)
    oppenheimerlabel.place(x=200, y=300, anchor=CENTER)
    oppenvissza = Button(topoppen, bootstyle="danger", style="danger.TButton", text="VISSZA", width=30, command=visszaoppen)
    oppenvissza.place(x=500, y=600, anchor=CENTER)
    oppentovabb = Button(topoppen, bootstyle="danger", style="danger.TButton", text="TOVÁBB A FOGLALÁSRA", width=30, command=foglalas)
    oppentovabb.place(x=750, y=600, anchor=CENTER)
    oppencim = Label(topoppen, text="Oppenheimer", foreground="#e34b54", font=('Ariel', 18), background="black")
    oppencim.place(x=400, y=110)
    oppenleiras = Label(topoppen, text="Bemutató ideje: 20 július 2023 , Játékidő: 181 perc, Korhatár: 16, Műfaj: Életrajzi, dráma", foreground="#e34b54", font=('Ariel', 14), background="black")
    oppenleiras.place(x=400, y=150)
    oppenszoveg = Label(topoppen, text="A Christopher Nolan által írt és rendezett Oppenheimer egy IMAX-re forgatott nagyszabású thriller. \nBerepíti a nézőt abba az izgalmas paradoxonba, amit az a rejtélyes férfi élt át, aki megkockáztatta,\nhogy elpusztítja a világot, azért, hogy megmentse azt. A főszereplők Cillian Murphy mint J. Robert\nOppenheimer, és Emily Blunt mint a felesége, a biológus és botanikus Katherine “Kitty” Oppenheimer.\nAz Oscar-díjas Matt Damon alakítja Leslie Groves Jr. tábornokot, a Manhattan-terv igazgatóját, és\nRobert Downey, Jr. alakítja Lewis Strausst, az Amerikai Atomenergia Bizottság alapító biztosát. Az\nOscar-jelölt Florence Pugh játssza Jean Tatlock pszichiátert, Benny Safdie Teller Ede elméleti fizikust,\nMichael Angarano Robert Serbert, valamint Josh Hartnett alakítja az úttörő amerikai atomtudóst,\nErnest Lawrence-et. A szereplők közt találjuk még az Oscar-díjas Rami Malekot, és a rendező ismét\negyütt dolgozik a nyolcszoros Oscar-jelölt színésszel, íróval és rendezővel, Kenneth Branagh-gel. A\nfilm Kai Bird és a néhai Martin J. Sherwin Pulitzer-díjas könyve, az Amerikai Prométheus: J. Robert\nOppenheimer diadala és tragédiája alapján készült. A producerek Emma Thomas, Charles Roven és\nChristopher Nolan.", foreground="#e34b54", font=('Ariel', 14), background="black")
    oppenszoveg.place(x=400, y=190)

def reszletekmost():
    global mostkep2, topmost
    topmost=Toplevel()
    topmost.iconbitmap("J:\IKT\Mozijegyfoglalo\kiskep.ico")
    topmost.geometry("1300x650")
    topmost.title("Részletek")
    topmost.resizable(False, False)
    topmost.configure(background="black")
    mostkep2 = PhotoImage(file="J:\IKT\Mozijegyfoglalo\mozijegy\mostvagysohanagy.png")
    mostlabel2 = Label(topmost, image=mostkep2, borderwidth=0)
    mostlabel2.place(x=200, y=300, anchor=CENTER)
    mostvissza = Button(topmost, bootstyle="danger", style="danger.TButton", text="VISSZA", width=30, command=visszamost)
    mostvissza.place(x=500, y=600, anchor=CENTER)
    mosttovabb = Button(topmost, bootstyle="danger", style="danger.TButton", text="TOVÁBB A FOGLALÁSRA", width=30, command=foglalas)
    mosttovabb.place(x=750, y=600, anchor=CENTER)
    mostcim = Label(topmost, text="Most vagy soha!", foreground="#e34b54", font=('Ariel', 18), background="black")
    mostcim.place(x=400, y=110)
    mostleiras = Label(topmost, text="bemutató ideje: 14 március 2024 , játékidő: 135 perc, Korhatár: 12, Műfaj: Akció, Dráma, Történelmi film", foreground="#e34b54", font=('Ariel', 14), background="black")
    mostleiras.place(x=400, y=150)
    mostszoveg = Label(topmost, text="Amikor 1848. március 15-én a lánglelkű költő, Petőfi Sándor költeményével, a Nemzeti Dallal\nkirobbantja a magyar forradalmat, az osztrák elnyomók egy titkosügynököt bíznak meg a feladattal,\nhogy állítsa meg a felkelést.", foreground="#e34b54", font=('Ariel', 14), background="black")
    mostszoveg.place(x=400, y=190)


def reszletekdune():
    global dunekep2, topdune
    topdune=Toplevel()
    topdune.iconbitmap("J:\IKT\Mozijegyfoglalo\kiskep.ico")
    topdune.geometry("1300x650")
    topdune.title("Részletek")
    topdune.resizable(False, False)
    topdune.configure(background="black")
    dunekep2 = PhotoImage(file="J:\IKT\Mozijegyfoglalo\mozijegy\dune2nagy.png")
    dunelabel2 = Label(topdune, image=dunekep2, borderwidth=0)
    dunelabel2.place(x=200, y=300, anchor=CENTER)
    dunevissza = Button(topdune, bootstyle="danger", style="danger.TButton", text="VISSZA", width=30, command=visszadune)
    dunevissza.place(x=500, y=600, anchor=CENTER)
    dunetovabb = Button(topdune, bootstyle="danger", style="danger.TButton", text="TOVÁBB A FOGLALÁSRA", width=30, command=foglalas)
    dunetovabb.place(x=750, y=600, anchor=CENTER)
    dunecim = Label(topdune, text="Dűne - Második rész", foreground="#e34b54", font=('Ariel', 18), background="black")
    dunecim.place(x=400, y=110)
    duneleiras = Label(topdune, text="Bemutató ideje: 29 február 2024 , Játékidő: 166 perc, Korhatár: 16, Műfaj: Sci-Fi", foreground="#e34b54", font=('Ariel', 14), background="black")
    duneleiras.place(x=400, y=150)
    duneszoveg = Label(topdune, text="A távoli jövőben, a bolygóközi királyságok korában játszódó történetben két nagyhatalmú uralkodóház\nharcol az Arrakis bolygó feletti hatalomért, mert az ismert univerzumban egyedül az itteni végtelen\nsivatagban bányászható az a fűszer, amely lehetővé teszi a csillagközi utazást. A Harkonnenek ura\nkiirtatta az Atreides családot. De Paul Atreides herceg (Timothée Chalamet) megmenekült: a\npusztaságban bujkál egy titokzatos, nomád nép, a fremenek között, ahol megismerkedik egy lánnyal,\nCsanival (Zendaya). Az a sorsa, hogy bosszút álljon a családjáért, háborúba vezesse a hozzá hű\nseregeket. Döntenie kell, hogy élete nagy szerelmét választja-e, vagy beteljesíti a végzetét. Az\nuniverzum sorsa múlik azon, hogy mit határoz: és végül olyan útra lép, amely megváltoztathatja azt a\nszörnyű jövőt, amelyet egyedül ő lát előre.", foreground="#e34b54", font=('Ariel', 14), background="black")
    duneszoveg.place(x=400, y=190)

def reszletekmehesz():
    global meheszkep2, topmehesz
    topmehesz=Toplevel()
    topmehesz.iconbitmap("J:\IKT\Mozijegyfoglalo\kiskep.ico")
    topmehesz.geometry("1300x650")
    topmehesz.title("Részletek")
    topmehesz.resizable(False, False)
    topmehesz.configure(background="black")
    meheszkep2 = PhotoImage(file="J:\IKT\Mozijegyfoglalo\mozijegy\mehesznagy.png")
    meheszlabel = Label(topmehesz, image=meheszkep2, borderwidth=0)
    meheszlabel.place(x=200, y=300, anchor=CENTER)
    meheszvissza = Button(topmehesz, bootstyle="danger", style="danger.TButton", text="VISSZA", width=30, command=visszamehesz)
    meheszvissza.place(x=500, y=600, anchor=CENTER)
    mehesztovabb = Button(topmehesz, bootstyle="danger", style="danger.TButton", text="TOVÁBB A FOGLALÁSRA", width=30, command=foglalas)
    mehesztovabb.place(x=750, y=600, anchor=CENTER)
    meheszcim = Label(topmehesz, text="A méhész", foreground="#e34b54", font=('Ariel', 18), background="black")
    meheszcim.place(x=400, y=110)
    meheszleiras = Label(topmehesz, text="Bemutató ideje: 11 január 2024 , játékidő: 105 perc, Korhatár: 16, Műfaj: Akció", foreground="#e34b54", font=('Ariel', 14), background="black")
    meheszleiras.place(x=400, y=150)
    meheszszoveg = Label(topmehesz, text="Egy férfi egyszemélyes, brutális bosszúhadjáratának tétje országos szintűre nő, miután kiderül róla,\nhogy korábban a Méhészek néven ismert befolyásos és titkos szervezet ügynöke volt.", foreground="#e34b54", font=('Ariel', 14), background="black")
    meheszszoveg.place(x=400, y=190)

def reszletekgk():
    global gkkep2, topgk
    topgk=Toplevel()
    topgk.iconbitmap("J:\IKT\Mozijegyfoglalo\kiskep.ico")
    topgk.geometry("1300x650")
    topgk.title("Részletek")
    topgk.resizable(False, False)
    topgk.configure(background="black")
    gkkep2 = PhotoImage(file="J:\IKT\Mozijegyfoglalo\mozijegy\godzilakongnagy.png")
    gklabel = Label(topgk, image=gkkep2, borderwidth=0)
    gklabel.place(x=200, y=300, anchor=CENTER)
    gkvissza = Button(topgk, bootstyle="danger", style="danger.TButton", text="VISSZA", width=30, command=visszagk)
    gkvissza.place(x=500, y=600, anchor=CENTER)
    gktovabb = Button(topgk, bootstyle="danger", style="danger.TButton", text="TOVÁBB A FOGLALÁSRA", width=30, command=foglalas)
    gktovabb.place(x=750, y=600, anchor=CENTER)
    gkcim = Label(topgk, text="Godzilla x Kong: Az új birodalom", foreground="#e34b54", font=('Ariel', 18), background="black")
    gkcim.place(x=400, y=110)
    gkleiras = Label(topgk, text="bemutató ideje: 28 március 2024 , játékidő: 115 perc, Műfaj: Kalandfilm, Fantasy", foreground="#e34b54", font=('Ariel', 14), background="black")
    gkleiras.place(x=400, y=150)
    gkszoveg = Label(topgk, text="A mindent eldöntő, minden eddiginél nagyobb háború nem ért véget azzal, hogy Kong és Godzilla\nszembetalálkozott és összemérte az erejét. Mert az ember most már kénytelen belenyugodni, hogy\nnem ő a legerősebb a földön. És nem ismeri igazán a saját világát: várja még néhány eddig rejtve\nmaradt meglepetés. Bujkál még valami a föld alatt, ami felébredt, és pusztítani akar. Az emberiség\nképtelen megállítani. Talán Kong is képtelen volna. És Godzilla is. De ha ők ketten összefognának,\nakkor esetleg megmenekülhetnének ők is és mi is…", foreground="#e34b54", font=('Ariel', 14), background="black")
    gkszoveg.place(x=400, y=190)
    
def belepes():
    global oppenheimerkep, dunekep, mostkep, meheszkep, godzillakep, kiskep
    topk=Toplevel()
    topk.iconbitmap("J:\IKT\Mozijegyfoglalo\kiskep.ico")
    topk.geometry("1300x650")
    topk.resizable(False, False)
    topk.title("Filmek")
    topk.configure(background="black")
    filmektabla=Label(topk, text="Választható filmek:", foreground="#e34b54", font=('Ariel', 20), background="black") 
    filmektabla.place(x=650, y=100, anchor=CENTER)

    kiskep = Image.open("J:\IKT\Mozijegyfoglalo\mozijegy\popcorntownfinalkicsi.png")
    kiskep = ImageTk.PhotoImage(kiskep) 
    image_label = Label(topk, image=kiskep) 
    image_label.place(x=1210, y=70, anchor=CENTER)
    
    dunekep = PhotoImage(file="J:\IKT\Mozijegyfoglalo\mozijegy\dune2.png")
    dunelabel = Label(topk, image=dunekep , borderwidth=0)
    dunelabel.place(x=650, y=300, anchor=CENTER)
    oppenheimerkep = PhotoImage(file="J:\IKT\Mozijegyfoglalo\mozijegy\oppenheimer.png")
    oppenheimerlabel = Label(topk, image=oppenheimerkep , borderwidth=0)
    oppenheimerlabel.place(x=150, y=300, anchor=CENTER)
    mostkep = PhotoImage(file="J:\IKT\Mozijegyfoglalo\mozijegy\mostvagysoha.png")
    mostlabel = Label(topk, image=mostkep , borderwidth=0)
    mostlabel.place(x=400, y=300, anchor=CENTER)
    meheszkep = PhotoImage(file="J:\IKT\Mozijegyfoglalo\mozijegy\mehesz.png")
    meheszlabel = Label(topk, image=meheszkep , borderwidth=0)
    meheszlabel.place(x=900, y=300, anchor=CENTER)
    godzillakep = PhotoImage(file="J:\IKT\Mozijegyfoglalo\mozijegy\godzilakong.png")
    godzillalabel = Label(topk, image=godzillakep , borderwidth=0)
    godzillalabel.place(x=1150, y=300, anchor=CENTER)
    
    oppenheimerreszletek = Button(topk, bootstyle="danger", style="danger.TButton", text="RÉSZLETEK", width=30, command=reszletekoppen)
    oppenheimerreszletek.place(x=150, y=500, anchor=CENTER)
    mostreszletek = Button(topk, bootstyle="danger", style="danger.TButton", text="RÉSZLETEK", width=30, command=reszletekmost)
    mostreszletek.place(x=400, y=500, anchor=CENTER)
    dunereszletek = Button(topk, bootstyle="danger", style="danger.TButton", text="RÉSZLETEK", width=30, command=reszletekdune)
    dunereszletek.place(x=650, y=500, anchor=CENTER)
    meheszreszletek = Button(topk, bootstyle="danger", style="danger.TButton", text="RÉSZLETEK", width=30, command=reszletekmehesz)
    meheszreszletek.place(x=900, y=500, anchor=CENTER)
    godzillareszletek = Button(topk, bootstyle="danger", style="danger.TButton", text="RÉSZLETEK", width=30, command=reszletekgk)
    godzillareszletek.place(x=1150, y=500, anchor=CENTER)
    
    dunefoglalas = Button(topk, bootstyle="danger", style="danger.TButton", text="FOGLALÁS", width=30, command=foglalas)
    dunefoglalas.place(x=650, y=540, anchor=CENTER)
    oppenheimerfoglalas = Button(topk, bootstyle="danger", style="danger.TButton", text="FOGLALÁS", width=30, command=foglalas)
    oppenheimerfoglalas.place(x=150, y=540, anchor=CENTER)
    mostfoglalas = Button(topk, bootstyle="danger", style="danger.TButton", text="FOGLALÁS", width=30, command=foglalas)
    mostfoglalas.place(x=400, y=540, anchor=CENTER)
    meheszfoglalas = Button(topk, bootstyle="danger", style="danger.TButton", text="FOGLALÁS", width=30, command=foglalas)
    meheszfoglalas.place(x=900, y=540, anchor=CENTER)
    godzillafoglalas = Button(topk, bootstyle="danger", style="danger.TButton", text="FOGLALÁS", width=30, command=foglalas)
    godzillafoglalas.place(x=1150, y=540, anchor=CENTER)
    


global oppenheimerkep, oppenheimerkep2, dunekep, dunekep2, mostkep, mostkep2, meheszkep, meheszkep2, godzillakep, gkkep2
ablak=Window(themename="vapor")
ablak.iconbitmap("J:\IKT\Mozijegyfoglalo\kiskep.ico")
ablak.resizable(False, False)
ablak.title("Mozifalva")
ablak.geometry("800x800")
ablak.configure(background="black")
logo = PhotoImage(file="J:\IKT\Mozijegyfoglalo\mozijegy\popcorntownfinal.png")
kep = Label(ablak, image=logo , borderwidth=0)
kep.place(x=400, y=300, anchor=CENTER)
mystyle=Style()
mystyle.configure("danger.TButton")
fogomb = Button(ablak, bootstyle="danger", style="danger.TButton", text="BELÉPÉS", width=30, command=belepes)
fogomb.place(x=400, y=700, anchor=CENTER)



ablak.mainloop()