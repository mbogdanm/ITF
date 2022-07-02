class ContBancar:
    #constructorul
    def __init__(self, titularCont, iban, departmentId, departmentName, ):
        #atribute, fields
        self.titularCont = titularCont
        self.iban = iban
        self.sold = 0
        self.activ = False
        self.incercari_activare = 0
        self.pin = 7777
    def __int__(self, departmentId, departmentName, employeeId, employeeName
    #metode
    def interogareSold(self):
        print(f'Titularul {self.titularCont}')
        print(f'IBAN {self.iban}')
        print(f'Sold {self.sold}')
        print(f'Activ {self.activ}')
        print(f'Nr de incercari {self.incercari_activare}')
        print('-------------------------------------------')

    def activareCont(self, pin_utilizator):
        print(f'Buna {self.titularCont}')
        if pin_utilizator == self.pin:
            print('Card activat cu SUCCES')
            self.activ = True
        else:
            print('PIN gresit')
            self.incercari_activare+=1

    def alimentareCont(self, suma):
        self.sold += suma
        print(f'Ati alimentat contul cu {suma} ')
        print(f'Aveti in cont {self.sold}')

    def plataCard(self, suma):
        self.salut()
        if suma <= self.sold:
            self.sold -= suma
            print(f'Ati cheltuit {suma}')
            print(f'Aveti in cont {self.sold}')
        else:
            print('Fonduri insuficiente')
    def salut(self):
        print(f'Buna {self.titularCont}')



