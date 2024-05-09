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
    
def btnclick():
    pass

def foglalas():
    global foglalablak
    foglalablak=Toplevel()
    foglalablak.iconbitmap("J:\IKT\Mozijegyfoglalo\kiskep.ico")
    foglalablak.geometry("1300x650")
    foglalablak.title("Foglalás")
    foglalablak.resizable(False, False)
    foglalablak.configure(background="black")
    style1 = Style()
    style1.configure("danger.TButton")
    style2 = Style()
    style2.configure("TButton")
    styl3 = Style()
    styl3.configure("TMenubutton")
    style4 = Style()
    style4.configure("warning.TButton")
    style5 = Style()
    style5.configure("info.TButton")
    frame4 = Frame(foglalablak, style='My.TFrame')
    frame4.pack()
    frame5 = Frame(foglalablak, style='My.TFrame')
    frame5.pack()

    label1 = Label(frame4, text='1.', font=("Ariel", 15, 'bold'), foreground='white', background='#e34b54')
    label1.grid(row=0,column=0, padx=(10,0))

    seat11 = Button(frame4, text='1', style='danger.TButton', command=lambda: btnclick(11))
    seat11.grid(row=0, column=1, padx=(10,5), pady=10)

    seat21 = Button(frame4, text='2', style='danger.TButton', command=lambda: btnclick(21))
    seat21.grid(row=0, column=2, padx=5, pady=10)

    seat31 = Button(frame4, text='3', style='danger.TButton', command=lambda: btnclick(31))
    seat31.grid(row=0, column=3, padx=5, pady=10)

    seat41 = Button(frame4, text='4', style='danger.TButton', command=lambda: btnclick(41))
    seat41.grid(row=0, column=4, padx=(5,25), pady=10)

    seat51 = Button(frame4, text='5', style='danger.TButton', command=lambda: btnclick(51))
    seat51.grid(row=0, column=5, padx=(25,5), pady=10)

    seat61 = Button(frame4, text='6', style='danger.TButton', command=lambda: btnclick(61))
    seat61.grid(row=0, column=6, padx=5, pady=10)

    seat71 = Button(frame4, text='7', style='danger.TButton', command=lambda: btnclick(71))
    seat71.grid(row=0, column=7, padx=5, pady=10)

    seat81 = Button(frame4, text='8', style='danger.TButton', command=lambda: btnclick(81))
    seat81.grid(row=0, column=8, padx=5, pady=10)

    seat91 = Button(frame4, text='9', style='danger.TButton', command=lambda: btnclick(91))
    seat91.grid(row=0, column=9, padx=(5,10), pady=10)

    label2 = Label(frame4, text='2.', font=("Ariel", 15, 'bold'), foreground='white', background='#e34b54')
    label2.grid(row=1,column=0, padx=(10,0))

    seat12 = Button(frame4, text='1', style='danger.TButton', command=lambda: btnclick(12))
    seat12.grid(row=1, column=1, padx=(10,5))

    seat22 = Button(frame4, text='2', style='danger.TButton', command=lambda: btnclick(22))
    seat22.grid(row=1, column=2, padx=5)

    seat32 = Button(frame4, text='3', style='danger.TButton', command=lambda: btnclick(32))
    seat32.grid(row=1, column=3, padx=5)

    seat42 = Button(frame4, text='4', style='danger.TButton', command=lambda: btnclick(42))
    seat42.grid(row=1, column=4, padx=(5,25))

    seat52 = Button(frame4, text='5', style='danger.TButton', command=lambda: btnclick(52))
    seat52.grid(row=1, column=5, padx=(25,5))

    seat62 = Button(frame4, text='6', style='danger.TButton', command=lambda: btnclick(62))
    seat62.grid(row=1, column=6, padx=5)

    seat72 = Button(frame4, text='7', style='danger.TButton', command=lambda: btnclick(72))
    seat72.grid(row=1, column=7, padx=5)

    seat82 = Button(frame4, text='8', style='danger.TButton', command=lambda: btnclick(82))
    seat82.grid(row=1, column=8, padx=5)

    seat92 = Button(frame4, text='9', style='danger.TButton', command=lambda: btnclick(92))
    seat92.grid(row=1, column=9, padx=(5,10))

    label3 = Label(frame4, text='3.', font=("Ariel", 15, 'bold'), foreground='white', background='#e34b54')
    label3.grid(row=2,column=0, padx=(10,0))

    seat13 = Button(frame4, text='1', style='danger.TButton', command=lambda: btnclick(13))
    seat13.grid(row=2, column=1, padx=(10,5), pady=10)

    seat23 = Button(frame4, text='2', style='danger.TButton', command=lambda: btnclick(23))
    seat23.grid(row=2, column=2, padx=5, pady=10)

    seat33 = Button(frame4, text='3', style='danger.TButton', command=lambda: btnclick(33))
    seat33.grid(row=2, column=3, padx=5, pady=10)

    seat43 = Button(frame4, text='4', style='danger.TButton', command=lambda: btnclick(43))
    seat43.grid(row=2, column=4, padx=(5,25), pady=10)

    seat53 = Button(frame4, text='5', style='danger.TButton', command=lambda: btnclick(53))
    seat53.grid(row=2, column=5, padx=(25,5), pady=10)

    seat63 = Button(frame4, text='6', style='danger.TButton', command=lambda: btnclick(63))
    seat63.grid(row=2, column=6, padx=5, pady=10)

    seat73 = Button(frame4, text='7', style='danger.TButton', command=lambda: btnclick(73))
    seat73.grid(row=2, column=7, padx=5, pady=10)

    seat83 = Button(frame4, text='8', style='danger.TButton', command=lambda: btnclick(83))
    seat83.grid(row=2, column=8, padx=5, pady=10)

    seat93 = Button(frame4, text='9', style='danger.TButton', command=lambda: btnclick(93))
    seat93.grid(row=2, column=9, padx=(5,10), pady=10)

    label4 = Label(frame4, text='4.', font=("Ariel", 15, 'bold'), foreground='white', background='#e34b54')
    label4.grid(row=3,column=0, padx=(10,0))

    seat14 = Button(frame4, text='1', style='danger.TButton', command=lambda: btnclick(14))
    seat14.grid(row=3, column=1, padx=(10,5))

    seat24 = Button(frame4, text='2', style='danger.TButton', command=lambda: btnclick(24))
    seat24.grid(row=3, column=2, padx=5)

    seat34 = Button(frame4, text='3', style='danger.TButton', command=lambda: btnclick(34))
    seat34.grid(row=3, column=3, padx=5)

    seat44 = Button(frame4, text='4', style='danger.TButton', command=lambda: btnclick(44))
    seat44.grid(row=3, column=4, padx=(5,25))

    seat54 = Button(frame4, text='5', style='danger.TButton', command=lambda: btnclick(54))
    seat54.grid(row=3, column=5, padx=(25,5))

    seat64 = Button(frame4, text='6', style='danger.TButton', command=lambda: btnclick(64))
    seat64.grid(row=3, column=6, padx=5)

    seat74 = Button(frame4, text='7', style='danger.TButton', command=lambda: btnclick(74))
    seat74.grid(row=3, column=7, padx=5)

    seat84 = Button(frame4, text='8', style='danger.TButton', command=lambda: btnclick(84))
    seat84.grid(row=3, column=8, padx=5)

    seat94 = Button(frame4, text='9', style='danger.TButton', command=lambda: btnclick(94))
    seat94.grid(row=3, column=9, padx=(5,10))

    label5 = Label(frame5, text='5.', font=("Ariel", 15, 'bold'), foreground='white', background='#e34b54')
    label5.grid(row=0,column=0, padx=(10,0))

    seat15 = Button(frame5, text='1', style='danger.TButton', command=lambda: btnclick(15))
    seat15.grid(row=0, column=1, padx=(10,5), pady=10)

    seat25 = Button(frame5, text='2', style='danger.TButton', command=lambda: btnclick(25))
    seat25.grid(row=0, column=2, padx=5, pady=10)

    seat35 = Button(frame5, text='3', style='danger.TButton', command=lambda: btnclick(35))
    seat35.grid(row=0, column=3, padx=5, pady=10)

    seat45 = Button(frame5, text='4', style='danger.TButton', command=lambda: btnclick(45))
    seat45.grid(row=0, column=4, padx=4, pady=10)

    seatblock = Button(frame5, text='+', style='danger.TButton', command=lambda: btnclick(00))
    seatblock.grid(row=0, column=5, padx=4, pady=10)

    seat55 = Button(frame5, text='5', style='danger.TButton', command=lambda: btnclick(55))
    seat55.grid(row=0, column=6, padx=4, pady=10)

    seat65 = Button(frame5, text='6', style='danger.TButton', command=lambda: btnclick(65))
    seat65.grid(row=0, column=7, padx=5, pady=10)

    seat75 = Button(frame5, text='7', style='danger.TButton', command=lambda: btnclick(75))
    seat75.grid(row=0, column=8, padx=5, pady=10)

    seat85 = Button(frame5, text='8', style='danger.TButton', command=lambda: btnclick(85))
    seat85.grid(row=0, column=9, padx=5, pady=10)

    seat95 = Button(frame5, text='9', style='danger.TButton', command=lambda: btnclick(95))
    seat95.grid(row=0, column=10, padx=(5,10), pady=10)

    

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
