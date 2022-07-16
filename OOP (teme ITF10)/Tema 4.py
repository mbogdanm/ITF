'''
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat',
'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
● ‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while.
'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

'● ‘Mașina mea preferată este x’.'
for i in range(len(masini)-1):
    print(f'Masina mea preferata esta {masini[i]}')

'● Fă același lucru cu un for each.'
for masina in masini:
    print(f'Masina mea preferata este {masina}')

'● Fă același lucru cu un while.'
i=0
while i < len(masini):
    print(f'Masina mea preferata este {masini[i]}')
    i+=1

'''
2. Aceeași listă:
Folosește un for else
În for

- Modifică elementele din listă astfel încât să fie scrie cu majuscule,
exceptând primul și ultimul.
În else:
- Printează lista.
'''

for masina in range(len(masini)):
    masini[masina] = masini[masina].upper()
else:
    print(masini)

'''3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘'''

for masina in masini:
    if masina == 'Mercedes':
        print(f'Am gasit masina dorita de dvs {masina}')
        break
    else:
        print(f'Am gasit masina {masina}. Mai cautam')

'''4. Aceași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
- Printează S-ar putea să vă placă mașina x.'''

for masina in masini:
    if masina == 'Trabant' or masina == 'Lăstun':
        continue
    print(f'S-ar putea sa va placa masina {masina}.')

'''
5. Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
● Printează Modele vechi: x.
● Modele noi: x.
'''

for i in range(len(masini)):
    if masini[i] == 'Trabant' or masini[i] == 'Lăstun':
        masini_vechi.append(masini[i])
        masini[i] = 'TESLA'
print(f'Masini vechi: {masini_vechi}')
print(f'Masini noi: {masini}')

'''
6. Având dict:
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000}

Vine un client cu un buget de 15000 euro.
● Prezintă doar mașinile care se încadrează în acest buget.
● Itereaza prin dict.items() și accesează mașina și prețul.
● Printează Pentru un buget de sub 15000 euro puteți alege mașină
xLastun
● Iterează prin listă.
'''
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000}
accesibil = 15000
for key, value in pret_masini.items():
    if value <= accesibil:
        print(f'Masina pe care ti-o permiti este {key}')

'''
7. Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
● Iterează prin ea.
● Afișează de câte ori apare 3 (nu ai voie să folosești count).
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
contor = 0
for numar in numere:
    if numar == 3:
        contor += 1
print(f'Cifra 3 apare de {contor} ori')
'''
8. Aceeași listă:
● Iterează prin ea
● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0
for numar in numere:
    suma += numar
print(f'Suma numerelor este {suma}')
'''
9. Aceeași listă:
● Iterează prin ea.
● Afișază cel mai mare număr (nu ai voie să folosești max).
'''
mare = 0
for numar in numere:
    if numar > mare:
        mare = numar
print(f'Cel mai mare numar {mare}')

'''
10. Aceeași listă:
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
● Afișază noua listă.
'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for numar in numere:
    if numar > 0:
       numere[numere.index(numar)] = -abs(numar)
print(numere)

# OPTIONALE #

'''
1.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere
Populează corect celelalte liste
Afișeaza cele 4 liste la final
'''
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for i in range(len(alte_numere)):
    if alte_numere[i] % 2 == 0:
        numere_pare.append(alte_numere[i])
    if alte_numere[i] % 2 != 0:
        numere_impare.append(alte_numere[i])
    if alte_numere[i] > 0:
        numere_pozitive.append(alte_numere[i])
    if alte_numere[i] < 0:
        numere_negative.append(alte_numere[i])
print(f'Numere pare:{numere_pare}')
print(f'Numere impare:{numere_impare}')
print(f'Numere pozitive{numere_pozitive}')
print(f'Numere pozitive{numere_negative}')

'''
2. Aceeași listă:
Ordonează crescător lista fară să folosești sort.
Te poți inspira vizual de aici.
https://www.youtube.com/watch?v=lyZQPjUT5B4
'''
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
temp = 0
lungimej = len(alte_numere)-1
lungimei = len(alte_numere)
for i in range(len(alte_numere)):
    for j in range(len(alte_numere)-1):
       if alte_numere[j] > alte_numere[j+1]:
           temp = alte_numere[j]
           alte_numere [j] = alte_numere[j+1]
           alte_numere [j+1] = temp
print(f'Lista ordonată: {alte_numere}')

'''
3. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
User alege un număr
Programul îi spune:
Nr secret e mai mare
Nr secret e mai mic
Felicitări! Ai ghicit!
'''

import random

ns = random.randint(1,30)
ng = None
print(ns)
while ng is None:
    nr = int(input('Introdu numarul:'))
    if nr > ns:
        print ('Numarul secret este mai mic')
    elif nr < ns:
        print ('Numarul secret ste mai are')
    else:
        print('Felicitari, ai gasit numarul!')
        break

'''
4.
'''
rows = 6
# if you want user to enter a number, uncomment the below line
# rows = int(input('Enter the number of rows'))
# outer loop
for i in range(rows):
    # nested loop
    for j in range(i):
        # display number
        print(i, end=' ')
    # new line after each row
    print('')
'''
5.
'''
tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print('Cifra curentă este:',tastatura_telefon[i][j])