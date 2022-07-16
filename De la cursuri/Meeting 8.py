# Abstractizare - concept prin care putem sa fortam o clasa copil sa defineasca un anumit comportament
# Polimorfism - concept prin care putem sa redefinim un comportament cu acelasi nume de metoda a.i. sa putem
    #sa oferim diversitate
# Encapsulare - concept prin care putem sa restrictionam accesul la datele noastre

# Mostenire vs Abstractizare:
    # Mostenirea nu forteaza reimplementarea anumitor metode in clasa copil
    # Abstractizarea forteaza reimplementarea

# Ca un fel de template. Obligam utilizatorul sa respecte un comportament.

from abc import ABC, \
    abstractmethod  # ABC = o clasa care mosteneste ABCmeta , ce defineste conceptul de abstractizare (interfata)

class Animal (ABC):

    @abstractmethod #decorator care marcheaza metoda ca fiind abstracta
    def sound(self):
        raise No

    #pass = cuvant cheie care defineste faptul ca corpul metodei nu are logica efectiva
        #dar este folosit pentru ca acea metoda sa poata sa aiba un CORP

    #raise NotImplementedError = modalitate prin care putem sa fortam in mod explicit exceptia de not implemented

    def sleep(self):
        raise NotImplementedError

#Atunci cand o clasa mosteneste o alta clasa de tip interfata sau clasa abstracta, spunem ca o implementeaza

class Dog(Animal):

    #def sound(self):
    #   print('Ham Ham!')
