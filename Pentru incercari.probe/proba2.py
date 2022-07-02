import datetime
from tabulate import tabulate

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

    # def genereaza_factura(self):
    #     print(f'Factura seria {self.SERIA} numar {self.numar} \n'
    #           f'Data: {datetime.date.today()} \n'
    #           f'PRODUS | CANTITATE | PRET BUCATA | TOTAL \n'
    #           f' {self.nume_produs}  |      {self.cantitate}      |     {self.pret_buc}    |     {self.pret_buc*self.cantitate}     ')

    def genereaza_factura(self):
        total = self.pret_buc*self.cantitate
        print(tabulate([[self.nume_produs, self.cantitate, self.pret_buc, total]],
                       headers = ['Produs', 'Cantitate', 'Pret bucata', 'Total']))

factura1 = Factura(3761, 'Mere', 3, 20)
factura2 = Factura(3862, 'Banane', 8, 33)
lista_obiecte = [factura1, factura2]
for obiect in lista_obiecte:
    obiect.genereaza_factura()

