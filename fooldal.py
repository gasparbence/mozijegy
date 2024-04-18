from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from ttkbootstrap import *


def visszao():
    global topro
    topro.destroy()

def visszad():
    global toprd
    toprd.destroy()
    

def reszletekoppen():
    global oppenheimerkep2, topro
    topro=Toplevel()
    topro.iconbitmap("kiskep.ico")
    topro.geometry("1300x650")
    topro.title("Részletek")
    topro.configure(background="black")
    oppenheimerkep2 = PhotoImage(file="J:\IKT\Mozijegyfoglalo\mozijegy\oppenheimernagy.png")
    oppenheimerlabel2 = Label(topro, image=oppenheimerkep2, borderwidth=0)
    oppenheimerlabel2.place(x=200, y=300, anchor=CENTER)
    oppenvissza = Button(topro, bootstyle="danger", style="danger.TButton", text="VISSZA", width=30, command=visszao)
    oppenvissza.place(x=500, y=600, anchor=CENTER)
    oppentovabb = Button(topro, bootstyle="danger", style="danger.TButton", text="TOVÁBB A FOGLALÁSRA", width=30)
    oppentovabb.place(x=750, y=600, anchor=CENTER)
    oppencim = Label(topro, text="Oppenheimer", foreground="red", font=('Ariel', 18), background="black")
    oppencim.place(x=400, y=110)
    oppenleiras = Label(topro, text="Bemutató ideje: 20 július 2023 , Játékidő: 181 perc, Korhatár: 16, Műfaj: Életrajzi, dráma", foreground="red", font=('Ariel', 14), background="black")
    oppenleiras.place(x=400, y=150)
    oppenszoveg = Label(topro, text="A Christopher Nolan által írt és rendezett Oppenheimer egy IMAX-re forgatott nagyszabású thriller. \nBerepíti a nézőt abba az izgalmas paradoxonba, amit az a rejtélyes férfi élt át, aki megkockáztatta,\nhogy elpusztítja a világot, azért, hogy megmentse azt. A főszereplők Cillian Murphy mint J. Robert\nOppenheimer, és Emily Blunt mint a felesége, a biológus és botanikus Katherine “Kitty” Oppenheimer.\nAz Oscar-díjas Matt Damon alakítja Leslie Groves Jr. tábornokot, a Manhattan-terv igazgatóját, és\nRobert Downey, Jr. alakítja Lewis Strausst, az Amerikai Atomenergia Bizottság alapító biztosát. Az\nOscar-jelölt Florence Pugh játssza Jean Tatlock pszichiátert, Benny Safdie Teller Ede elméleti fizikust,\nMichael Angarano Robert Serbert, valamint Josh Hartnett alakítja az úttörő amerikai atomtudóst,\nErnest Lawrence-et. A szereplők közt találjuk még az Oscar-díjas Rami Malekot, és a rendező ismét\negyütt dolgozik a nyolcszoros Oscar-jelölt színésszel, íróval és rendezővel, Kenneth Branagh-gel. A\nfilm Kai Bird és a néhai Martin J. Sherwin Pulitzer-díjas könyve, az Amerikai Prométheus: J. Robert\nOppenheimer diadala és tragédiája alapján készült. A producerek Emma Thomas, Charles Roven és\nChristopher Nolan.", foreground="red", font=('Ariel', 14), background="black")
    oppenszoveg.place(x=400, y=190)
    
def reszletekdune():
    global dunekep2, toprd
    toprd=Toplevel()
    toprd.iconbitmap("kiskep.ico")
    toprd.geometry("1300x650")
    toprd.title("Részletek")
    toprd.configure(background="black")
    dunekep2 = PhotoImage(file="J:\IKT\Mozijegyfoglalo\mozijegy\dune2nagy.png")
    dunelabel2 = Label(toprd, image=dunekep2, borderwidth=0)
    dunelabel2.place(x=200, y=300, anchor=CENTER)
    dunevissza = Button(toprd, bootstyle="danger", style="danger.TButton", text="VISSZA", width=30, command=visszad)
    dunevissza.place(x=500, y=600, anchor=CENTER)
    dunetovabb = Button(toprd, bootstyle="danger", style="danger.TButton", text="TOVÁBB A FOGLALÁSRA", width=30)
    dunetovabb.place(x=750, y=600, anchor=CENTER)
    dunecim = Label(toprd, text="Dűne - Második rész", foreground="red", font=('Ariel', 18), background="black")
    dunecim.place(x=400, y=110)
    duneleiras = Label(toprd, text="Bemutató ideje: 29 február 2024 , Játékidő: 166 perc, Korhatár: 16, Műfaj: Sci-Fi", foreground="red", font=('Ariel', 14), background="black")
    duneleiras.place(x=400, y=150)
    duneszoveg = Label(toprd, text="A távoli jövőben, a bolygóközi királyságok korában játszódó történetben két nagyhatalmú uralkodóház\nharcol az Arrakis bolygó feletti hatalomért, mert az ismert univerzumban egyedül az itteni végtelen\nsivatagban bányászható az a fűszer, amely lehetővé teszi a csillagközi utazást. A Harkonnenek ura\nkiirtatta az Atreides családot. De Paul Atreides herceg (Timothée Chalamet) megmenekült: a\npusztaságban bujkál egy titokzatos, nomád nép, a fremenek között, ahol megismerkedik egy lánnyal,\nCsanival (Zendaya). Az a sorsa, hogy bosszút álljon a családjáért, háborúba vezesse a hozzá hű\nseregeket. Döntenie kell, hogy élete nagy szerelmét választja-e, vagy beteljesíti a végzetét. Az\nuniverzum sorsa múlik azon, hogy mit határoz: és végül olyan útra lép, amely megváltoztathatja azt a\nszörnyű jövőt, amelyet egyedül ő lát előre.", foreground="red", font=('Ariel', 14), background="black")
    duneszoveg.place(x=400, y=190)
    
    
def belepes():
    global oppenheimerkep, dunekep, mostkep, meheszkep, godzillakep
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
    meheszkep = PhotoImage(file="J:\IKT\Mozijegyfoglalo\mozijegy\mehesz.png")
    meheszlabel = Label(topk, image=meheszkep , borderwidth=0)
    meheszlabel.place(x=900, y=300, anchor=CENTER)
    godzillakep = PhotoImage(file="J:\IKT\Mozijegyfoglalo\mozijegy\godzilakong.png")
    godzillalabel = Label(topk, image=godzillakep , borderwidth=0)
    godzillalabel.place(x=1150, y=300, anchor=CENTER)
    
    dunereszletek = Button(topk, bootstyle="danger", style="danger.TButton", text="RÉSZLETEK", width=30, command=reszletekdune)
    dunereszletek.place(x=650, y=500, anchor=CENTER)
    oppenheimerreszletek = Button(topk, bootstyle="danger", style="danger.TButton", text="RÉSZLETEK", width=30, command=reszletekoppen)
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
    


global oppenheimerkep, oppenheimerkep2, dunekep, dunekep2, mostkep, meheszkep, godzillakep
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