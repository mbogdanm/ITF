masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
masini_vechi=[]
for i in range(len(masini)):
    if masini[i] == 'Trabant' or masini[i] == 'Lăstun':
        masini_vechi.append(masini[i])
        masini[i] = 'TESLA'
    if masini[i] == 'TESLA':
        masini.remove('TESLA')
print(f'Masini vechi: {masini_vechi}')
print(f'Masini noi: {masini}')