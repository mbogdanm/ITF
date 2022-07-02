#---------EX 1-----------
'''
atata vreme cat conditia din if este TRUE, se executa codul din interiorul if-ului

else este statement-ul care contine cod ce va fi executat daca conditia din if este FALSE
'''

#---------EX 2-----------
x = int(input('Introdu numarul:'))
print('Numarul introdus este:',x)
if (x>=0):
    print ('\033[2;30;44mNumarul este natural.\033[0;0m')
else:
    print ('\033[2;30;31mNumarul nu este natural. Acesta este numar intreg.\033[0;0m')

#---------EX 3-----------
y = float(input('Introdu numarul:'))
print('\033[2;30;44mNumarul introdus este:\033[0;0m',y)
if (y==1):
    print('Numarul este numar neutru pentru inmultire si impartire.')
elif(y>0):
    print ('Acest numar este pozitiv')
elif(y<0):
    print ('Numarul este negativ.')
elif(y==0):
    print('Numarul este numar neutru pentru adunare.')

#---------EX 4-----------
z = int(input('Introdu numarul:'))
print('\033[2;30;44mNumarul introdus este:\033[0;0m',z)
print('Se verifica daca acest numar este in intervalul [-2, 13]')
time.sleep(3)
if (z>=-2 and z<=13):
    print('Toate supercomputerele spun ca ACEST NUMAR SE AFLA IN [-2, 13]')
    time.sleep(2)
    print('\033[1;30;43mWARNING!!! This program will self-destroy in...\033[0;0m')
    time.sleep(1)
    print('\r3...',end='')
    time.sleep(1)
    print('\r2..',end='')
    time.sleep(1)
    print('\r1.',end='')
    time.sleep(1)
    print('\r0', end='')
    time.sleep(1)
    print('\r\033[1;31;44mBOOM!!!\033[0;0m',end='')

else:
    print('Nu am reusit sa convingem niciun computer ca acest numar s-ar afla in intervalul [-2, 13].')
    time.sleep(2)
    print('\033[1;30;43mWARNING!!! This program will self-destroy in...\033[0;0m')
    time.sleep(1)
    print('\r3...',end='')
    time.sleep(1)
    print('\r2..',end='')
    time.sleep(1)
    print('\r1.',end='')
    time.sleep(1)
    print('\r0', end='')
    time.sleep(1)
    print('\033[1;31;44mBOOM!!!\033[0;0m')

#---------EX 5-----------
w = int(input('Type x:'))
print('x=',w)
v = int(input('Type y:'))
print('y=',v)
time.sleep(1)
print("We'll try to solve this problem of yours: x-y")
time.sleep(1)
print('Problem solved. The result: x-y =',w-v)
time.sleep(1)
if(w-v<5):
    print('The result is smaller than 5')
else:
    print('The result is not smaller than 5')

#---------EX 6-----------
a = int(input('X='))
if (not (a>=5 and a<=27) == True):
    print(not (a>=5 and a<=27))
    print('DA: Numarul NU se afla in interval')
else:
    print(not (a >= 5 and a <= 27))
    print('NU: Numarul se afla in interval')

#---------EX 7-----------
t = int(input('Type x:'))
print('x=',t)
u = int(input('Type y:'))
print('y=',u)
if (t==u):
    print('Numerele sunt egale')
elif (t>u):
    print('Numerele nu sunt egale')
    print(f'X={t} este mai mare')
elif (t<u):
    print('Numerele nu sunt egale')
    print(f'Y={u} este mai mare')

#---------EX 8-----------
j = int(input('Latura X = '))
print('x=',j)
k = int(input('Type y = '))
print('y=',k)
l = int(input('Type z = '))
print('y=',l)

if (j==k!=l or j!=k==l or j==l!=k):
    print('Triunghiul este isoscel')
elif (j==k==l):
    print('Triunghiul este echilateral')
elif (j!=k and k!=l and j!=l):
    print('Triunghiul este oarecare')

#---------EX 9-----------
litera =  str(input('Introdu o literă: '))
if litera in ('a','e','i','o','u','ă','â','î','A','E','I','O','U','Ă','Î','Â'):
    print (f'{litera} este vocală')
else:
    print(f'{litera} nu este vocală')

#---------EX 10-----------
nota = float(input('Nota = '))
if (nota>9):
    nota = 'A'
    print('Echivalentul în sistem american este:',nota)
elif (nota >= 8 and nota <= 9):
    nota = 'B'
    print('Echivalentul în sistem american este:',nota)
elif (nota >= 7 and nota < 8):
    nota = 'C'
    print('Echivalentul în sistem american este:', nota)
elif (nota >= 6 and nota < 7):
    nota = 'D'
    print('Echivalentul în sistem american este:', nota)
elif (nota > 4 and nota < 6):
    nota = 'E'
    print('Echivalentul în sistem american este:', nota)
elif (nota <= 4):
    nota = 'F'
    print('Echivalentul în sistem american este:', nota)

# -------------- EXERCITII OPTIONALE --------------- #
#EX 1
x = int(input('X = '))
if (len(str(x))>=4):
    print (f'Numarul X are minim 4 cifre')
else:
    print('Numarul are mai putin de 4 cifre')

#EX 2
x = int(input('X = '))
if (len(str(x))==6):
    print (f'Numarul X are exact 6 cifre')
else:
    print('Numarul nu are exact 6 cifre')

#EX 3
x = int(input('X = '))
if(x%2 == 0):
    print (f'X ({x}) este număr par')
else:
    print (f'X ({x}) nu este număr par')

#EX 4
j = int(input('x = '))
print('x=',j)
k = int(input('y = '))
print('y=',k)
l = int(input('z = '))
print('Z=',l)

if (j>k and j>l):
    print (f'X = {j} este cel mai mare număr')
elif (k>j and k>l):
    print (f'Y = {k} este cel mai mare număr')
elif (l>k and l>j):
    print(f'Z = {l} este cel mai mare număr')

#EX 5
x = int(input('Unghiul A = '))
print('A = ',x,'°')
y = int(input('Unghiul B = '))
print('B = ',y,'°')
z = int(input('Unghiul C = '))
print('C = ',z,'°')

if (x+y+z == 180):
    print('Suma unghiurilor este exact 180°')
    print('Triunghi valid')
else:
    print('Suma unghiurilor NU este exact 180°')
    print('Nu este triungi')


