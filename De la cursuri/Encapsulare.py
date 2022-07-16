#O modalitate prin care putem sa restrictionam accesul la anumite
    # atribute sau metode

#Exista 3 TIPURI de acces prin care se poate implementa encapsularea
    # PUBLIC = atributul sau metoda sunt vizibile sau accesibile de oriunde - se defineste ca atare
    # PRIVATE = atributul sau metoda sunt accesibile sau vizibile doar din CLASA curenta
        # se poate implementa cu ajutorul semnului "__" inaintea atributului sau metodei
    # PROTECTED = atributul sau metoda sunt accesibile sau vizibile oriunde in PACHETUL curent
        # se poate implementa cu ajutorul semnului "_" inaintea atributului sau metodei
            #pachetul se defineste prin intermediul unui folder "Python Package" care contine
            #fisierul


class Car:
    __color = 'Gray' # variabila PRIVATE
    # _variabila_protected = "Test"
    #
    # def __init__(self, var_protected):
    #     self._variabila_protected = var_protected

    def get_color(self): #folosim getter sa afisam culoarea
        return self.__color

    def set_color(self, culoare): #folosim setter sa atribuim o culoare
        self.__color = culoare

    def delete_color(self):
        self.__color = None

    def __hidden(self):
        print(self._variabila_protected)


volvo = Car()
print(volvo.get_color())#getter
volvo.set_color('red') #setter
print(volvo.get_color())#getter
volvo.delete_color()#deleter
print(volvo.get_color())#getter

