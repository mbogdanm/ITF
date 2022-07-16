'''1.Funcție care să calculeze și să returneze suma a două numere'''

def suma_numere(n1,n2):
    suma = n1 + n2
    return suma
print(suma_numere(10,2))

'''2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar'''

def par_impar(n):
    if n%2 == 0:
        return True
    else:
        return False
print(par_impar(4))

'''3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)'''

def nr_caractere(nume):
    return len(nume)-len(' ')
print(nr_caractere('Bogdan Mihalcea'))

'''4. Funcție care returnează aria dreptunghiului'''

def aria_dreptunghi(latime, lungime):
    a = latime*lungime
    return a
print(aria_dreptunghi(2,7))

'''5. Funcție care returnează aria cercului'''

import math
def arie_cerc(raza):
    a = math.pi*raza**2
    return a
print(arie_cerc(7))

'''6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
și False dacă nu găsește.'''

def caracter(sir):
    for c in sir:
        if sir[sir.index(c)] == 'x':
            return True
        else:
            pass
    return False
print(caracter('Este un x in acest sir?'))

'''7. Funcție fără return, primește un string și printează pe ecran:
● Nr de caractere lower case este x
● Nr de caractere upper case exte'''

def caractere_lower(sir):
    countl = 0
    countu = 0
    for c in sir:
        if c.islower():
            countl += 1
        elif c.isupper():
            countu += 1
    print('Nr de caractere lower case este', countl)
    print('Nr de caractere upper case este', countu)

caractere_lower('Abba ESTE o formatie')

'''8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
numerele pozitive'''
pozitive = []
def lista_numere(lista):
    for n in lista:
        if lista[lista.index(n)] > 0:
            pozitive.append(n)
    return pozitive
print(lista_numere(lista=[7,-2,3,6,-1,-3]))

'''9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
● Primul număr x este mai mare decat al doilea nr y
● Al doilea nr y este mai mare decat primul nr x
● Numerele sunt egale.'''

def comparatie(x,y):
    if x>y:
        print(f'Primul numar {x} este mai mare decat {y}')
    elif x<y:
        print(f'Al doi-lea numar {y} este mai mare decat {x}')
    else:
        print('Numerele sunt egale')
comparatie(7,2)

'''10. Funcție care primește un număr și un set de numere.
● Printeaza ‘am adaugat numărul nou în set’ + returnează True
● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
returnează False'''

def seturi(n,set):
    if n not in set:
        set.add(n)
        print('Am adaugat numarul nou in set',set)
        return True
    elif n in set:
        print('Numarul exista deja in set', set)
        return False
print(seturi(7,{2,3}))

'''___________________________O-P-T-I-O-N-A-L-E___________________________'''

'''1. Funcție care primește o lună din an și returnează câte zile are acea luna'''

from datetime import date
def data(month):
    data1 = date(2022,month,1)
    data2 = date(2022,month+1,1)
    rezultat = data2-data1
    return rezultat.days
print(data(month=2))

''''''



