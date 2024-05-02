from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from ttkbootstrap import *



#def szekek():
#    global foglalablak
#    szekekbtn = {}
#    for i in range(1, 4):
#        szekekbtn[f"szekbtn{i}"] = Button(foglalablak, bootstyle="danger", style="danger.TButton", width=10)

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

def foglalas():
    global foglalablak
    foglalablak=Toplevel()
    foglalablak.iconbitmap("J:\IKT\Mozijegyfoglalo\kiskep.ico")
    foglalablak.geometry("1300x650")
    foglalablak.title("Foglalás")
    foglalablak.resizable(False, False)
    foglalablak.configure(background="black")
    #szekek()
    

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
    oppencim = Label(topoppen, text="Oppenheimer", foreground="red", font=('Ariel', 18), background="black")
    oppencim.place(x=400, y=110)
    oppenleiras = Label(topoppen, text="Bemutató ideje: 20 július 2023 , Játékidő: 181 perc, Korhatár: 16, Műfaj: Életrajzi, dráma", foreground="red", font=('Ariel', 14), background="black")
    oppenleiras.place(x=400, y=150)
    oppenszoveg = Label(topoppen, text="A Christopher Nolan által írt és rendezett Oppenheimer egy IMAX-re forgatott nagyszabású thriller. \nBerepíti a nézőt abba az izgalmas paradoxonba, amit az a rejtélyes férfi élt át, aki megkockáztatta,\nhogy elpusztítja a világot, azért, hogy megmentse azt. A főszereplők Cillian Murphy mint J. Robert\nOppenheimer, és Emily Blunt mint a felesége, a biológus és botanikus Katherine “Kitty” Oppenheimer.\nAz Oscar-díjas Matt Damon alakítja Leslie Groves Jr. tábornokot, a Manhattan-terv igazgatóját, és\nRobert Downey, Jr. alakítja Lewis Strausst, az Amerikai Atomenergia Bizottság alapító biztosát. Az\nOscar-jelölt Florence Pugh játssza Jean Tatlock pszichiátert, Benny Safdie Teller Ede elméleti fizikust,\nMichael Angarano Robert Serbert, valamint Josh Hartnett alakítja az úttörő amerikai atomtudóst,\nErnest Lawrence-et. A szereplők közt találjuk még az Oscar-díjas Rami Malekot, és a rendező ismét\negyütt dolgozik a nyolcszoros Oscar-jelölt színésszel, íróval és rendezővel, Kenneth Branagh-gel. A\nfilm Kai Bird és a néhai Martin J. Sherwin Pulitzer-díjas könyve, az Amerikai Prométheus: J. Robert\nOppenheimer diadala és tragédiája alapján készült. A producerek Emma Thomas, Charles Roven és\nChristopher Nolan.", foreground="red", font=('Ariel', 14), background="black")
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
    mostcim = Label(topmost, text="Most vagy soha!", foreground="red", font=('Ariel', 18), background="black")
    mostcim.place(x=400, y=110)
    mostleiras = Label(topmost, text="bemutató ideje: 14 március 2024 , játékidő: 135 perc, Korhatár: 12, Műfaj: Akció, Dráma, Történelmi film", foreground="red", font=('Ariel', 14), background="black")
    mostleiras.place(x=400, y=150)
    mostszoveg = Label(topmost, text="Amikor 1848. március 15-én a lánglelkű költő, Petőfi Sándor költeményével, a Nemzeti Dallal\nkirobbantja a magyar forradalmat, az osztrák elnyomók egy titkosügynököt bíznak meg a feladattal,\nhogy állítsa meg a felkelést.", foreground="red", font=('Ariel', 14), background="black")
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
    dunecim = Label(topdune, text="Dűne - Második rész", foreground="red", font=('Ariel', 18), background="black")
    dunecim.place(x=400, y=110)
    duneleiras = Label(topdune, text="Bemutató ideje: 29 február 2024 , Játékidő: 166 perc, Korhatár: 16, Műfaj: Sci-Fi", foreground="red", font=('Ariel', 14), background="black")
    duneleiras.place(x=400, y=150)
    duneszoveg = Label(topdune, text="A távoli jövőben, a bolygóközi királyságok korában játszódó történetben két nagyhatalmú uralkodóház\nharcol az Arrakis bolygó feletti hatalomért, mert az ismert univerzumban egyedül az itteni végtelen\nsivatagban bányászható az a fűszer, amely lehetővé teszi a csillagközi utazást. A Harkonnenek ura\nkiirtatta az Atreides családot. De Paul Atreides herceg (Timothée Chalamet) megmenekült: a\npusztaságban bujkál egy titokzatos, nomád nép, a fremenek között, ahol megismerkedik egy lánnyal,\nCsanival (Zendaya). Az a sorsa, hogy bosszút álljon a családjáért, háborúba vezesse a hozzá hű\nseregeket. Döntenie kell, hogy élete nagy szerelmét választja-e, vagy beteljesíti a végzetét. Az\nuniverzum sorsa múlik azon, hogy mit határoz: és végül olyan útra lép, amely megváltoztathatja azt a\nszörnyű jövőt, amelyet egyedül ő lát előre.", foreground="red", font=('Ariel', 14), background="black")
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
    meheszcim = Label(topmehesz, text="A méhész", foreground="red", font=('Ariel', 18), background="black")
    meheszcim.place(x=400, y=110)
    meheszleiras = Label(topmehesz, text="Bemutató ideje: 11 január 2024 , játékidő: 105 perc, Korhatár: 16, Műfaj: Akció", foreground="red", font=('Ariel', 14), background="black")
    meheszleiras.place(x=400, y=150)
    meheszszoveg = Label(topmehesz, text="Egy férfi egyszemélyes, brutális bosszúhadjáratának tétje országos szintűre nő, miután kiderül róla,\nhogy korábban a Méhészek néven ismert befolyásos és titkos szervezet ügynöke volt.", foreground="red", font=('Ariel', 14), background="black")
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
    gkcim = Label(topgk, text="Godzilla x Kong: Az új birodalom", foreground="red", font=('Ariel', 18), background="black")
    gkcim.place(x=400, y=110)
    gkleiras = Label(topgk, text="bemutató ideje: 28 március 2024 , játékidő: 115 perc, Műfaj: Kalandfilm, Fantasy", foreground="red", font=('Ariel', 14), background="black")
    gkleiras.place(x=400, y=150)
    gkszoveg = Label(topgk, text="A mindent eldöntő, minden eddiginél nagyobb háború nem ért véget azzal, hogy Kong és Godzilla\nszembetalálkozott és összemérte az erejét. Mert az ember most már kénytelen belenyugodni, hogy\nnem ő a legerősebb a földön. És nem ismeri igazán a saját világát: várja még néhány eddig rejtve\nmaradt meglepetés. Bujkál még valami a föld alatt, ami felébredt, és pusztítani akar. Az emberiség\nképtelen megállítani. Talán Kong is képtelen volna. És Godzilla is. De ha ők ketten összefognának,\nakkor esetleg megmenekülhetnének ők is és mi is…", foreground="red", font=('Ariel', 14), background="black")
    gkszoveg.place(x=400, y=190)
    
def belepes():
    global oppenheimerkep, dunekep, mostkep, meheszkep, godzillakep, kiskep
    topk=Toplevel()
    topk.iconbitmap("J:\IKT\Mozijegyfoglalo\kiskep.ico")
    topk.geometry("1300x650")
    topk.resizable(False, False)
    topk.title("Filmek")
    topk.configure(background="black")
    filmektabla=Label(topk, text="Választható filmek:", foreground="red", font=('Ariel', 20), background="black") 
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