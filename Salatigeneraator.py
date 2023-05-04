from tkinter import *
from tkinter import ttk
import random
from typing import List
#Vaja rahvusk88ki, hinnaklassi, koostisosa tüüpi, kas taimene, kas ühe koostisosa eri vormid
k88gid = ["FUSION", "Ladina-Ameerika", "Aafrika", "Prantsusmaa",
          "Itaalia", "Kreeka", "Lähis-Ida", "Aasia"]
#toiduaine = ["Nimi",
#             sobivad köögid,
#             hinnaklass,
#             ", täpsustus",
#             ", täpsustus"]

rukola = ["Rukola",
          [k88gid[0], k88gid[1], k88gid[2], k88gid[3], k88gid[4], k88gid[5]],
          1]

beebispinat = ["Beebispinat",
               [k88gid[0], k88gid[3], k88gid[4], k88gid[5]],
               1]

lehtkapsas = ["Lehtkapsas",
              k88gid,
              2]

peedilehed = ["Peedilehed",
              [k88gid[0], k88gid[3]],
              1]

paktsoi = ["Paktsoi",
           [k88gid[0], k88gid[7]],
           2]

roomakapsas = ["Roomakapsas",
              [k88gid[0], k88gid[1], k88gid[2], k88gid[3], k88gid[4], k88gid[5], k88gid[6]],
              2]

frillis = ["Frillis",
           [k88gid[0], k88gid[1], k88gid[3], k88gid[4], k88gid[5]],
           1]

hiinakapsas = ["Hiinakapsas",
               [k88gid[0], k88gid[7]],
               0]

voilillelehed = ["Võilillelehed",
                 [k88gid[0], k88gid[3]],
                 0]

rohelus = [rukola, beebispinat, lehtkapsas, peedilehed, paktsoi,
           roomakapsas, frillis, hiinakapsas, voilillelehed, 0, 2]
##########################################################################

kurk = ["Kurk",
        k88gid,
        1]

kartul = ["Kartul",
          k88gid,
          0,
          ", küpsetatud",
          ", praetud"]

paprika = ["Paprika",
           k88gid,
           1,
           ", õhukesed viilud",
           ", grillitud"]


kapsas = ["Kapsas",
          k88gid,
          0,
          ", tükeldatud",
          ", viilutatud"]



kapsas = ["Kapsas",
          k88gid,
          0,
          ", tükeldatud",
          ", viilutatud"]

porgand = ["Porgand, riivitud",
           k88gid,
           0,]

peet = ["Peet",
        [k88gid[0], k88gid[2], k88gid[3], k88gid[4], k88gid[5]],
        0,
        ", aurutatud",
        ", küpsetatud"]

maapirn = ["Maapirn, küpseatud",
           [k88gid[0], k88gid[3], k88gid[4], k88gid[6]],
           2]

suvikorvits = ["Suvikõrvits",
               k88gid,
               1,
               ", viilutatud",
               ", küpsetatud"]

korvits = ["Kõrvits, küpsetatud",
           k88gid,
           1]

avokaado = ["Avokaado",
            [k88gid[0], k88gid[1]],
            2]

redis = ["Redis",
         [k88gid[0], k88gid[2], k88gid[3], k88gid[7]],
         1]

seened = ["Seened, praetud",
          [k88gid[0], k88gid[1], k88gid[2], k88gid[3], k88gid[4], k88gid[5], k88gid[6]],
          2]

mais = ["Keedetud mais",
        [k88gid[0], k88gid[1]],
        1]

k88giviljad = [kurk, kartul, paprika, kapsas,
               porgand, porgand, peet, maapirn, suvikorvits,
               korvits, avokaado, redis, seened, mais, 2, 4]
##########################################################################

sinihallitusjuust = ["Sinihallitusjuust",
                     [k88gid[0], k88gid[3], k88gid[4]],
                     1]

parmesan = ["Parmesan",
            [k88gid[0], k88gid[4]],
            2]

maitseparm = ["Maitsepärm, helbed",
              k88gid,
              0]

feta = ["Feta",
        [k88gid[0], k88gid[1], k88gid[2], k88gid[3], k88gid[4], k88gid[5]],
        2]

kuuslauk = ["Küüslauk, viilutatud, praetud",
            k88gid,
            0]

sibul = ["Sibul",
         k88gid,
         0,
         ", punane",
         ", roheline",
         ", röstitud"]

basiilik = ["Basiilik",
            [k88gid[0], k88gid[3], k88gid[4], k88gid[5]],
            2]

oliivid = ["Oliivid",
           [k88gid[0], k88gid[3], k88gid[4], k88gid[5], k88gid[6]],
           2]


maitsekas = [sinihallitusjuust, parmesan, maitseparm, feta,
             kuuslauk, sibul, basiilik, oliivid, 1, 1]

##########################################################################

paevalilleseemned = ["Päevalilleseemned",
                     [k88gid[0], k88gid[3], k88gid[6], k88gid[7]],
                     0]

korvitsaseemned = ["Kõrvitsaseemned",
                   k88gid,
                   1]

seesamiseemned = ["Seesamiseemned",
                  [k88gid[0], k88gid[2], k88gid[6], k88gid[7]],
                  0]

linaseemned = ["Linaseemned",
               [k88gid[0], k88gid[3], k88gid[4]],
               0]

indiapahkel = ["India pählid",
               [k88gid[0], k88gid[6], k88gid[7]],
               2,
               ", terved",
               ", röstitud"]

kreekapahkel = ["Kreeka pähklid",
                [k88gid[0], k88gid[3], k88gid[4], k88gid[5], k88gid[6]],
                2]

pistaatsiapahkel = ["Pistaatsiapähklid",
                    [k88gid[0], k88gid[3], k88gid[4], k88gid[5], k88gid[6]],
                    2]

parapahkel = ["Parapähklid",
              [k88gid[0], k88gid[1]],
              2]

maapahkel = ["Maapähklid, röstitud",
             [k88gid[0], k88gid[2], k88gid[6], k88gid[7]],
             0]

metspahkel = ["Metspähklid",
              [k88gid[0], k88gid[3], k88gid[4]],
              2]

pekaanipahkel = ["Pekaanipähklid",
                 [k88gid[0], k88gid[1], k88gid[3], k88gid[4], k88gid[5], k88gid[6]],
                 2]


seeme = [paevalilleseemned, korvitsaseemned, seesamiseemned, linaseemned,
               indiapahkel, kreekapahkel, pistaatsiapahkel, parapahkel,
               maapahkel, metspahkel, pekaanipahkel, 0, 1]

##########################################################################

bulgur = ["Bulgur",
          [k88gid[0], k88gid[2], k88gid[6]],
          0]

kusskuss = ["Kusskuss",
            [k88gid[0], k88gid[2], k88gid[4], k88gid[6]],
            0]

tatar = ["Tatar",
         [k88gid[0], k88gid[3]],
         0]

riis = ["Riis",
        [k88gid[0], k88gid[1], k88gid[2], k88gid[4], k88gid[5], k88gid[6], k88gid[7]],
        0]

odrakruup = ["Odrakruup",
             [k88gid[0], k88gid[3]],
             0]

krutoonid = ["Krutoonid",
             [k88gid[0], k88gid[3], k88gid[4], k88gid[5]],
             0]

orzo = ["Orzo",
        [k88gid[0], k88gid[4]],
        1]

makaronid = ["Makaronid",
            [k88gid[0], k88gid[4]],
            0]


sorgo = ["Sorgo",
            [k88gid[0], k88gid[1], k88gid[2], k88gid[6]],
            0]

kinoa = ["Kinoa",
            [k88gid[0], k88gid[1], k88gid[2]],
            2]

teravili = [bulgur, kusskuss, tatar, riis, odrakruup, krutoonid, orzo, makaronid, sorgo, kinoa, 0, 1]

##########################################################################

laatsed = ["Läätsed",
           [k88gid[0], k88gid[1], k88gid[3], k88gid[6]],
           0]

kikerherned = ["Kikerherned, röstitud",
               [k88gid[0], k88gid[2], k88gid[4], k88gid[6]],
               0]

oad = ["Oad",
       [k88gid[0], k88gid[1], k88gid[2], k88gid[6]],
       0]

tofu = ["Tofu",
        [k88gid[0], k88gid[7]],
        1]

suitsulohe = ["Suitsulõhe",
              [k88gid[0], k88gid[3], k88gid[7]],
              2]

muna = ["Muna",
        k88gid,
        0,
        ", keedetud",
        ", praetud",
        ", poseeritud"]


valk = [laatsed, kikerherned, oad, 
        tofu, suitsulohe, muna, 0, 1]

##########################################################################

marineeritudsibul = ["Marineeritud punane sibul",
                     [k88gid[0], k88gid[1], k88gid[2], k88gid[5], k88gid[6]],
                     0]

marineeritudkurk = ["Marineeritud kurk",
                    [k88gid[0], k88gid[3], k88gid[6]],
                    0]

kimchi = ["Kimchi",
          [k88gid[0], k88gid[7]],
          1]

tomat = ["Tomat",
         [k88gid[0], k88gid[1], k88gid[2], k88gid[3], k88gid[4], k88gid[5], k88gid[6]],
         1]

kirsstomat = ["Tomat",
              [k88gid[0], k88gid[1], k88gid[2], k88gid[3], k88gid[4], k88gid[5], k88gid[6]],
              2]

jalapeno = ["Marineeritud jalapeno",
            [k88gid[0], k88gid[1]],
            1]

hapu = [marineeritudsibul, marineeritudkurk, kimchi,
        tomat, kirsstomat, jalapeno, 1, 1]

##########################################################################

apelsin = ["Apelsin",
           [k88gid[0], k88gid[1], k88gid[3], k88gid[4], k88gid[5], k88gid[6]],
           1]

mandariin = ["Apelsin",
             [k88gid[0], k88gid[3], k88gid[4], k88gid[5], k88gid[6]],
             1]

ananass = ["Ananass",
           [k88gid[0], k88gid[1], k88gid[2], k88gid[7]],
           1,
           ", tükeldatud",
           ", grillitud"]

oun = ["Õun",
       [k88gid[0], k88gid[3], k88gid[7]],
       0,
       ", küpsetatud",
       ", tükeldatud"]

pirn = ["Pirn",
        [k88gid[0], k88gid[7]],
        0,
        ", küpsetatud",
        ", tükeldatud"]

granaatounaseemned = ["Granaatõunaseemned",
                      k88gid,
                      2]

kumkvaat = ["Kumkvaat",
            [k88gid[0], k88gid[3], k88gid[4], k88gid[5], k88gid[6]],
            2]

viinamarjad = ["Viinamarjad",
               [k88gid[0], k88gid[1], k88gid[3], k88gid[4], k88gid[5]],
               1]

kiivi = ["Kiivi",
         [k88gid[0], k88gid[1]],
         1]

mango = ["Mango",
         [k88gid[0], k88gid[1], k88gid[2], k88gid[7]],
         1]
melon = ["Melon",
         [k88gid[0], k88gid[1], k88gid[2], k88gid[7]],
          1]

kreegid = ["Kreegid",
           [k88gid[0], k88gid[3]],
           1]

magus = [apelsin, mandariin, ananass, oun,
         pirn, granaatounaseemned, kumkvaat, viinamarjad, kiivi, mango, melon, kreegid, 0, 1]

##########################################################################

pesto = ["Pesto",
         [k88gid[0],k88gid[4]],
         1]

sojakaste = ["Sojakaste",
             [k88gid[0], k88gid[7]],
             0]

misopasta = ["Misopasta",
             [k88gid[0], k88gid[7]],
             0]

rosmariin = ["Rosmariin",
             [k88gid[0], k88gid[3], k88gid[4], k88gid[5], k88gid[6]],
             0]

kuuslauk2 = ["Küüslauk",
             k88gid,
             0]

seesamioli = ["Seesamiõli",
              [k88gid[0], k88gid[2], k88gid[6], k88gid[7]],
              1]

maitseparm2 = ["Maitsepärm",
               k88gid,
               0]

koriander = ["Koriandrilehed",
             [k88gid[0], k88gid[1], k88gid[7]],
             1]

kasteMaitsekas = [pesto, sojakaste, misopasta, rosmariin, kuuslauk2, seesamioli, maitseparm2, koriander, 1, 1]

##########################################################################

mesi = ["Mesi",
        k88gid,
        0]

moos = ["Moos",
        [k88gid[0], k88gid[3]],
        0]

sriracha = ["Sriracha",
            [k88gid[0], k88gid[1]],
            1]

kasteMagusVürtsikas = [mesi, moos, sriracha, 0, 1]

##########################################################################

ounaaadikas = ["Õunaäädikas",
               [k88gid[0], k88gid[1], k88gid[2], k88gid[3], k88gid[5]],
               0]

riisiveiniaadikas = ["Riisiveiniäädikas",
                     [k88gid[0], k88gid[7]],
                     0]

palsamiaadikas = ["Palsamiäädikas",
                  [k88gid[0], k88gid[3], k88gid[4]],
                  1]

tamarind = ["Tamarindipasta",
            [k88gid[0], k88gid[7]],
            1]

sinep = ["Sinep",
         [k88gid[0], k88gid[3], k88gid[4], k88gid[5], k88gid[6]],
         1]

laim = ["Laimimahl",
        [k88gid[0], k88gid[1], k88gid[2], k88gid[6]],
        0]

sidrun = ["Sidruniimahl",
        [k88gid[0], k88gid[1], k88gid[2], k88gid[4], k88gid[5], k88gid[6]],
        0]

kasteHapu = [ounaaadikas, riisiveiniaadikas, palsamiaadikas, tamarind, sinep, laim, sidrun, 1, 1]

##########################################################################

oliivioli = ["Oliiviõli",
             [k88gid[0], k88gid[1], k88gid[2], k88gid[3], k88gid[4], k88gid[5], k88gid[6]],
             0]

avokaadoõli = ["Avokaadoõli",
               [k88gid[0], k88gid[1]],
               2]

maapahklivoi = ["Maapähklivõi",
                [k88gid[0], k88gid[2], k88gid[3], k88gid[7]],
                1]

tahini = ["Tahini",
          [k88gid[0], k88gid[2], k88gid[5], k88gid[6]],
          1]

indiapahklivoi = ["Indiapähklivõi",
                  [k88gid[0], k88gid[2], k88gid[3], k88gid[7]],
                  2]

majonees = ["Majonees",
            [k88gid[0], k88gid[3]],
            0]


kasteRasv = [oliivioli, avokaadoõli, maapahklivoi, tahini, indiapahklivoi, majonees, 1, 1]

salatiOsad = [rohelus, k88giviljad, maitsekas, seeme, teravili, valk, hapu, magus]
kastmeOsad = [kasteMaitsekas, kasteMagusVürtsikas, kasteHapu, kasteRasv]
koostisosad = salatiOsad + kastmeOsad
##########################################################################

def generaator(minRaha, maxRaha, k88k):                                                    #Funktsioon, mis genereerib salati
    hind = 0
    while hind >= maxRaha or hind <= minRaha:
        hind = 0
        valitudSalat: List[object] = []
        valitudKaste: List[object] = []
        valitud: List[object] = []
        for el in salatiOsad:
            valitudFinal: List[object] = []
            arv = random.randint(el[-2], el[-1])
            while len(valitudFinal) < arv:
                pakutav = el[random.randint(0,len(el)-3)]
                if k88k in pakutav[1] and pakutav[0] not in valitud:
                    hind += pakutav[2]
                    valitud.append(pakutav[0])
                    if len(pakutav) == 3:
                        valitudFinal.append(pakutav[0])
                    else:
                        valitudFinal.append(pakutav[0]+pakutav[random.randint(3,len(pakutav)-1)])
            valitudSalat += valitudFinal
            
        for el in kastmeOsad:
            valitudFinal: List[object] = []
            arv = random.randint(el[-2], el[-1])
            while len(valitudFinal) < arv:
                pakutav = el[random.randint(0,len(el)-3)]
                if k88k in pakutav[1] and pakutav[0] not in valitud:
                    hind += pakutav[2]
                    valitud.append(pakutav[0])
                    if len(pakutav) == 3:
                        valitudFinal.append(pakutav[0])
                    else:
                        valitudFinal.append(pakutav[0]+pakutav[random.randint(3,len(pakutav)-1)])
            valitudKaste += valitudFinal
            
            retsept = k88k + " stiilis salat\n\nSalat:\n\n" + "\n".join(valitudSalat) + "\n\nKaste:\n\n" + "\n".join(valitudKaste)
    return retsept
            
        
    
def salat():                                                      #Funktsioon, kui vajutad "Submit"
    #Sätib eelarve
    maxRaha = 0
    if var.get() == 0:
        minRaha = 0
        maxRaha = 4
    elif var.get() == 1:
        minRaha = 4
        maxRaha = 8
    else:
        minRaha = 8
        maxRaha = 20
    #Valib rahvusköögi suvaliselt kasutaja valikute seast
    tuple = valikud.curselection()
    valik = list(tuple)
    k88k = k88gid[valik[random.randint(0,len(valik)-1)]]
    #Teeb uue akna retseptiga
    aken = Toplevel(root)
    aken.title("Retsept")
    raam = Frame(aken)
    raam.grid(row=0, column=0, padx=5, pady=5)
    retseptiKoht = ttk.Label(raam, text = generaator(minRaha, maxRaha, k88k))
    retseptiKoht.grid(column=0, row=0)
    
#Teeb akna
root = Tk()
root.title("Salatigeneraator")
var = IntVar()
frm = Frame(root)
frm.grid(row=0, column=0, padx=5, pady=5)

#Eelarve nupud
label = ttk.Label(frm, text="Milline on sinu salatieelarve?")
label.grid(column=0, row=0)
r1 = Radiobutton(frm, text = "madal", variable = var, value = 0)
r1.grid(column=0, row=1)
r2 = Radiobutton(frm, text = "keskmine", variable = var, value = 1)
r2.grid(column=0, row=2)
r3 = Radiobutton(frm, text = "kõrge", variable = var, value = 2)
r3.grid(column=0, row=3)

#Rahvusköökide valik
label2 = ttk.Label(frm, text="Milliste rahvusköökide salateid te täna genereerida soovite?")
label2.grid(column=0, row=4)
var2 = IntVar()
valikud = Listbox(frm, selectmode = "multiple")
valikud.grid(column=0, row=5)
for each_item in range(len(k88gid)):
    valikud.insert(END, k88gid[each_item])

#Submit nupp, käivitab funktsiooni
B = Button(frm, text="Submit", command = salat)
B.grid(column=0, row=6)
root.update()


root.mainloop()
