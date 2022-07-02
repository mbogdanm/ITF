try:
    lista = [1,5,3]
    print(lista[3])
except IndexError as e:
    print('Index out of bound exception')
    print(e)

try:
    n = 0
    calcul = 10/n
except Exception as e:
    print('Nu se poate imparti la 0')
    print(e)