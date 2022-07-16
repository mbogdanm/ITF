"""
ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
probabil am colturi’
"""
from abc import ABC, abstractmethod


class FormaGeometrica(ABC): #clasa parinte care contine atributul latura si constructorul pentru aceasta

    PI = 3.14
    __latura = None
    __raza = None

    @abstractmethod
    def aria(self):
        #pass
        raise NotImplementedError #posibilitatea de a implementa calculul ariei - oblig clasele ce mostenesc formageometrica

    def descrie(self):
        print('Cel mai probabil am colturi')


"""INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură"""

"""
ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
implementezi metoda abstractă aria)
"""


class Patrat(FormaGeometrica): #clasa copil care mosteneste clasa FormaGeometrica (atribut si constructor)


    def __init__(self, latura):
        self.__latura = latura

    def construieste_patrat(self):
        print(f'Patratul are latura: {self.__latura}')

    def aria(self):
        aria = self.__latura**2
        return aria

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f'Latura este de {self.__latura}')

    @latura.setter
    def latura(self, latura):
        self.__latura = latura

    @latura.deleter
    def latura (self):
        self.__latura = None


patrat1 = Patrat(7)
patrat2 = Patrat(40)
patrat1.construieste_patrat()
print(patrat1.aria())
#getter
patrat2.latura
#setter
patrat2.latura = 2
#getter
patrat2.latura
#deleter
del patrat2.latura
#getter
patrat2.latura

"""
Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI
mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
abstractă aria)
"""

class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__raza = raza

    def aria(self):
        aria = self.PI * self.__raza**2
        return aria

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Raza cercului este: {self.__raza}')

    @raza.setter
    def raza(self, raza):
        self.__raza = raza

    @raza.deleter
    def raza(self):
        self.__raza = None

cerc1 = Cerc(7)
#getter
cerc1.raza
#setter
cerc1.raza = 6
#getter
cerc1.raza
print(cerc1.aria())
#deleter
del cerc1.raza
#getter
cerc1.raza

