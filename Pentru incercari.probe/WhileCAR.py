#dalmatieni
for i in range(0,102, 10):
    print(f'Dalmatianul cu numarul {i}')

numere = [3, 7, 13, 72]
#parcurgere lista cu for prin intermediul indexului
s = 0
for i in range(0, len(numere)):
    print(f'Numarul este {numere[i]}')

for numar in numere:
    print(f'Numarul curent este {numar}')
    s += numar
print('Suma este ',s)