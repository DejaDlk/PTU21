# 3 Užduotis
# Padaryti paleidžiamąjį failą iš 11 paskaitos 4 programos (pilna programa su vartotojo sąsaja)
# Programa turi turėti programos lango ikoną ir norimą pavadinimą
# Paleidžiamasis failas turi turėti norimą ikoną


from tkinter import *

langas = Tk()
# susikuriam STRINGVAR tam, kad galetume atkurti buvusi teksta, su paprastu kintamuoju NEVEIKIA: (naudojam isvalyti ir atkurti)
atkurti_paskutini = StringVar()

def atspausdina():
    rezultatas["text"] = f"Labas, {ivedimo_laukas.get()} !"
    spausdinam["text"] = "Sukurta"

def isvalyti():
    atkurti_paskutini.set(ivedimo_laukas.get())
    ivedimo_laukas.delete(0, END)
    spausdinam["text"] = "Išvalyta"

def atkurti():
    ivedimo_laukas.insert(0, atkurti_paskutini.get())
    spausdinam["text"] = "Atkurta"

def iseiti():
    langas.destroy()


vardas = Label(langas, text="Iveskite varda")
ivedimo_laukas = Entry(langas)
mygtukas = Button(langas, text="Patvirtinti", command=atspausdina)
rezultatas = Label(langas, text="")
spausdinam = Label(langas, text="")

vardas.grid(row=0, column=0)
ivedimo_laukas.grid(row=0,column=1)
mygtukas.grid(row=0, column=2)
# columnspan - kai norime lygiuoti centre atsakyma, tai darom su columnpan (pradedam skaiciuoti nuo 1 (cia sujunge 3 stulp)):
rezultatas.grid(row=1, columnspan=3)
# LAMBDA - F-ja lambda naudojame argumentams perduoti kitoms funkcijoms, kurios vykdomos paspaudus bet kurį mygtuką, siuo atveju ENTER/ESC:
langas.bind("<Return>", lambda x: atspausdina())
langas.bind("<Escape>", lambda x: iseiti())
spausdinam.grid(row=2, columnspan=3, sticky=W+E)

# kuriam meniu:
meniu = Menu(langas)
langas.config(menu=meniu)
# tearoff leidzia sukurti submeniu pagrindiniame Meniu:
submeniu = Menu(meniu, tearoff = 0)

meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Išvalyti", command=isvalyti)
submeniu.add_command(label="Atkurti", command=atkurti)
# sukuriam linijyte po submeniu isvalyti ir atkurti:
submeniu.add_separator()
submeniu.add_command(label="Išeiti", command=iseiti)

langas.mainloop()

# FAILAS YRA :
# C:\Users\Dell\PycharmProjects\pythonProject2\13_3_UZDUOTIS\dist
