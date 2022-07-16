"""
1.Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()
"""
import math


class Cerc:  # am creat raza Cerc

    raza = None  # atribute de obiecte de clasa
    culoare = 'Default'

    def __init__(self, raza, culoare):  # am facut constructorul pentru raza

        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):  # metoda pentru a printa culoarea si raza cercului

        print(f'Cercul are culoarea: {self.culoare}')
        print(f'Raza cercului este: {self.raza} cm')

    def aria(self):  # metoda pentru calcul arie cerc

        return print(f'Aria cercului este: {self.raza ** 2 * math.pi} cm^2')

    def diametru(self):
        return print(f'Diametrul cercului este: {self.raza * 2} cm')

    def circumferunta(self):
        return print(f'Circumferinta cercului este: {self.raza * 2 * math.pi} cm')


cerc1 = Cerc(raza=7, culoare='Rosu')
cerc2 = Cerc(raza=8, culoare='Galben')
cerc1.descrie_cerc()
cerc1.aria()
cerc1.diametru()
cerc1.circumferunta()
cerc2.descrie_cerc()

'''
2. Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
'''


class Dreptunghi:
    lungime = None
    latime = None
    culoare = 'Default'

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f'Lungime dreptunghi: {self.lungime}')
        print(f'Latime dreptunghi: {self.latime}')
        print(f'Culoare dreptunghi: {self.culoare}')

    def aria(self):
        return print(f'Aria dreptunghiului: {self.lungime * self.latime}')

    def perimetru(self):
        return print(f'Perimetrul dreptunghiului: {2 * (self.lungime + self.latime)}')

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare


dreptunghi1 = Dreptunghi(lungime=7, latime=2, culoare='Verde')
dreptunghi1.descrie()
dreptunghi1.aria()
dreptunghi1.perimetru()
dreptunghi1.schimba_culoarea(noua_culoare='Albastru')
dreptunghi1.descrie()

'''
3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)
'''


class Angajat:
    nume = 'Default'
    prenume = 'Default'
    salariu = None

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f'Nume: {self.nume}')
        print(f'Prenume: {self.prenume}')
        print(f'Salariu: {self.salariu}')

    def nume_complet(self):
        print(f'Nume complet: {self.nume} {self.prenume}')

    def salariu_lunar(self):
        print(f'Salariu lunar: {self.salariu}')

    def salariu_anual(self):
        print(f'Salariu anual: {self.salariu * 12}')

    def marire_salariu(self,procent):
        print(f'Salariul tau dupa marire este de {self.salariu*procent}')


angajat1 = Angajat(nume='Mihalcea', prenume='Bogdan', salariu=7000)
angajat1.descrie()
angajat1.nume_complet()
angajat1.salariu_lunar()
angajat1.salariu_anual()

"""
4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)
"""


class Cont:
    iban = 'Default'
    titular_cont = 'Default'
    sold = None

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} Soldul tau este: {self.sold}')

    def debitare_cont(self, suma):
        self.sold = self.sold - suma
        return print(f'Soldult tau dupa debitarea sumei {suma} este {self.sold}')

    def creditare_cont(self, suma):
        self.sold = self.sold + suma
        return print(f'Soldul tau dupa creditarea sumei de {suma} este de {self.sold}')


cont1 = Cont(iban='ROBTLR1324700035', titular_cont='Bogdan Mihalcea', sold=300)
cont1.afisare_sold()
cont1.debitare_cont(suma=50)
cont1.afisare_sold()
cont1.creditare_cont(suma=1000)
cont1.afisare_sold()

""" ___________ OPTIONALE ____________ """

"""
1. Clasa Factura
Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
avea aceeași serie), număr, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
● schimbă_cantitatea(cantitate)
● schimbă_prețul(pret)
● schimbă_nume_produs(nume)
● generează_factura() - va printa tabelar dacă reușiți
Factura seria x numar y
Data: generați automat data de azi
Produs | cantitate | preț bucată | Total
Telefon | 7 | 700 | 49000
"""
import datetime

class Factura:
    SERIA = 'YU'
    numar = None
    nume_produs = 'Default'
    cantitate = None
    pret_buc = None

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate

    def schimba_pretul(self, pret):
        self.pret_buc = pret

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume

    def genereaza_factura(self):
        print(f'Factura seria {self.SERIA} numar {self.numar} \n'
              f'Data: {datetime.date.today()} \n'
              f'PRODUS | CANTITATE | PRET BUCATA | TOTAL \n'
              f' {self.nume_produs}  |      {self.cantitate}      |     {self.pret_buc}    |     {self.pret_buc*self.cantitate}     ')

factura1 = Factura(3761, 'Mere', 3, 20)
factura1.genereaza_factura()
factura1.schimba_pretul(25)
factura1.genereaza_factura()
factura1.schimba_cantitatea(10)
factura1.genereaza_factura()
factura1.schimba_nume_produs('Pere')
factura1.genereaza_factura()

"""
2.Clasa Masina
Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate mașinile cand ies din fabrica sunt gri
Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
Culori disponibile = alegeți voi 5-7 culori
Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
Inmatriculata = False
Constructor: model, viteza_maxima
Metode:
● descrie() - se vor printa toate atributele, în afară de culori_disponibile
● înmatriculare() - va schimba atributul înmatriculată în True
● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
culoare e în opțiunea de culori disponibile, altfel afișați o eroare
● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
accelera până la viteza maximă
● franeaza() - mașina se va opri și va avea viteza 0
"""

class Masina:
    MARCA = 'Jeep'
    model = 'Default'
    viteza_maxima = None
    viteza_actuala = 0
    culoare = 'Default'
    culori_disponibile = ('Rosu',
                          'Verde',
                          'Galben',
                          'Negru',
                          'Gri',
                          'Albastru')
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie(self):
        print(f'Masina {self.MARCA}, model {self.model}, are o viteza maxima de {self.viteza_maxima} \n'
              f'Aceasta se deplaseaza acum cu viteza de {self.viteza_actuala} km/h \n'
              f'Masina este de culoare {self.culoare}')

    def inmatriculare(self, inmatriculata):
        self.inmatriculata = inmatriculata

    def vopseste(self, culoare):
        if culoare in self.culori_disponibile:
            self.culoare = culoare
        else:
            print('Aceasta culoare nu este diponibila')
            pass

    def accelereaza(self, viteza): #functie care primeste o valoare in variabila viteza
        if viteza < self.viteza_maxima: #se verifica daca viteza primit este mai mica decat viteza maxima
            self.viteza_actuala = viteza #daca da, atunci viteza actuala va fi viteza
        elif viteza < 0: #daca viteza este negativa, atunci apare o eroare!
            print('EROARE! Masina merge in marsarier sau valoarea este gresita')
        else:
            self.viteza_actuala = self.viteza_maxima #daca viteza este mai mare decat viteza_max, viteza_actuala va fi
                                                        #limita de viteza

masina1 = Masina('Grand Cherokee RT', 230)

masina1.descrie()
masina1.inmatriculare(True)
masina1.vopseste('Roz')
masina1.accelereaza(205)
masina1.descrie()

"""
3. Clasa TodoList
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
Metode:

● adauga_task(nume, descriere) - se va adauga in dict
● finalizează_task(nume) - se va sterge din dict
● afișează_todo_list() - doar cheile
● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
printăm detalii suplimentare.
○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
adauge.
○ Dacă acesta răspunde nu - la revedere
○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
dict
"""

class ToDoList:
    dict = {}
