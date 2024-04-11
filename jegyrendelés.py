from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from ttkbootstrap import *


ablak=Window(themename="vapor")
ablak.resizable(False, False)
ablak.title("Mozifalva")
ablak.geometry("800x800")
ablak.configure(background="black")
canv2 = Canvas(ablak, width=400, height=400, bg='white')
canv2.grid(row=1, column=0)
kep3 = Image.open("./kepek/popcorntownfinal.png")
img2 = ImageTk.PhotoImage(kep3) 
canv2.create_image(20, 20, anchor=NW, image=img2)
mystyle=Style()
mystyle.configure("danger.TButton")

def belepes():
    topk=Toplevel()
    topk.geometry("400x400")
    topk.title("Filmek")
    filmektabla=Label(topk,text="Választható filmek:")
    filmektabla.grid(row=0, column=0)

fogomb = Button(ablak, bootstyle="danger", style="danger.TButton", text="BELÉPÉS", width=30, command=belepes)
fogomb.place(x=400, y=700, anchor=CENTER)




ablak.mainloop()