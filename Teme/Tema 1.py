#EX 1
'''
O variabilă este un loc alocat din memoria calculatorului in care pot fi stocate valori.
Variabilele sunt create când li se atribuie o valoare
'''
#EX 2
nume = 'Bogdan'
varsta = 33
inaltime = 1.88
python = True

#EX 3
print(type(nume,),type(varsta),type(inaltime),type(python))

#EX 4
inaltime=round(inaltime)

print(type(inaltime))

#EX 5
inaltime = 1.88
print(f'Eu ma numesc {nume}, am varsta de {varsta}. Inaltimea mea este de {inaltime}m. Imi place python? {python}')

#EX 6
nume = input('Nume: ')
prenume = input('Prenume: ')
print(f'Numele complet are', len(nume+prenume), 'caractere')

#EX 7
lungimea = int(input('Lungimea: '))
latimea = int(input('Lățimea: '))

print(f'Aria dreptunghiului este:', (lungimea*latimea), 'metri pătrați.')

#EX 8
fraza = 'Coral is either the stupidest animal or the smartest rock'
pozitie = int(input('X: '))
print(fraza[0:len(fraza)-pozitie])

#EX 9
#a.
str1 = str(fraza[0:5]+fraza[len(fraza)-5::])
print(str1)
#b.
print('Cuvantul the apare de',fraza.count('the'),'ori')
#c.
d=fraza.replace('the','THE',)
print(d)
#d.
index = fraza.index('rock')
str2 = str(fraza[0:index])
print('Indexul cuvantului rock incepe cu: ',index)
print(str2)

#EX 10
sir = input('Introdu stringul: ')
assert sir[0:1] == sir[len(sir)-1:len(sir)]

#EX 11
sirnr = '0123456789'
print('Numere pare:',sirnr[2::2])
print('Numere impare:',sirnr[1::2])

#EX 12
assert type(fraza) == int

#   -- EXERCITII OPTIONALE --

#EX 1

sirImpar = input('Introdu stringul de dimensiune impara: ')
if len(sirImpar)%2 != 0:
    print(sirImpar[int(len(sirImpar)/2):int((len(sirImpar)/2)+1):])
else:
    print('Nu ai introdus un string de lungime para')

#EX 2
palindrom = input('Introdu stringul de verificat:')
assert palindrom[::1] == palindrom [::-1]

#EX 3
a,b = input('Baga string:').split()
print(a)
print(b)

#EX 4
capitalize = input('String pentru exercitiul 4:')
k = capitalize[1::]