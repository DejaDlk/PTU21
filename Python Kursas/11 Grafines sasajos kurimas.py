# 1 užduotis, Sukurti programą su grafine sąsaja, kuri:
# Turėtų laukelį su užrašu "Įveskite vardą", kuriame vartotojas galėtų įvesti vardą
# Turėtų mygtuką su užrašu "Patvirtinti", kurį nuspaudus, programa po lauku atspausdintų "Labas, {vardas}!"

# 2 užduotis
# Patobulinti 1 užduoties programą, kad ji:
# Atspausdintų pasisveikinimą ne tik nuspaudus mygtuką, bet ir paspaudus mygtuką "Enter"

# 3 užduotis
# Patobulinti 2 užduoties programą, kad ji turėtų meniu pavadinimu "Meniu", kuriame:
# Būtų punktas "Išvalyti", kurį paspaudus išsitrintų tekstas eilutėje, kurioje spausdinamas pasisveikinimo tekstas
# Būtų punktas "Atkurti", kurį paspaudus pasisveikinimo teksto eilutėje butų atspausdintas paskutinis atspausdintas tekstas
# Būtų punktas "Išeiti", kurį paspaudus užsidarytų programos langas
# Tarp menių punktų "Atkurti" ir "Išeiti" būtų atskyrimo brūkšnys

# 4 užduotis
# Patobulinti 3 užduoties programą, kad ji turėtų statuso juostą apačioje, kurioje:
# Būtų rodoma "Sukurta", kai atspausdinamas pasisveikinimo tekstas
# Būtų rodoma "Išvalyta", kai ištrinamas pasisveikinimo tekstas
# Būtų rodoma "Atkurta", kai atkuriamas paskutinis pasisveikinimo tekstas Nuspaudus klaviatūros mygtuką "Escape", uždarytų programos langą

# GRID - lengviau naudoti, jei reikia išdėstyti daiktus tinklelyje
# PACK - lengviau naudoti, jei tereikia kai kuriuos valdiklius sudėti į vieną eilutę arba vieną stulpelį.

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






# 5 užduotis (papildoma)
# Perdaryti bet kurią sukurtą arba savo programą, kurioje vartotojas turėjo įvesti duomenis, į programą su grafine sąsaja.
# Pvz., tą, kuri atrenka keliamuosius metus, skaičiuoja laiką nuo praeitos datos, pateikia info apie įvestą eilutę ar pan.

from tkinter import *

langas = Tk()

def patikrinimas():
        # int rasom, kad ivestu sveika skaiciu:
        metu_ivedimas = int(ivedimo_laukas.get())
        if (metu_ivedimas % 4 ==0) or (metu_ivedimas % 100 == 0) or (metu_ivedimas % 400 == 0):
            atspausdinam["text"] = f"{metu_ivedimas} yra keliamieji metai"
        else:
            atspausdinam["text"] = f"{metu_ivedimas} yra nekeliamieji metai"

def iseiti():
# destroy - uzdaro visa cikla
    langas.destroy()

# kuriam langa su mygtukais:
ivedimas = Label(langas, text="Iveskite metus")
ivedimo_laukas =Entry(langas)
mygtukas1 = Button(langas, text="Patikrinti", command=patikrinimas)
atspausdinam = Label(langas, text="")

# isvedam kur bus mygtukai ir pridedam enter ir esc opcijas:
ivedimas.grid(row=0, column=0)
ivedimo_laukas.grid(row=0, column=1)
mygtukas1.grid(row=0, column=2)
atspausdinam.grid(row=1, columnspan=3)
# LAMBDA - F-ja lambda naudojame argumentams perduoti kitoms funkcijoms, kurios vykdomos paspaudus bet kurį mygtuką, siuo atveju ENTER/ESC:
langas.bind("<Return>", lambda x: patikrinimas())
langas.bind("<Escape>", lambda x: iseiti())

langas.mainloop()
