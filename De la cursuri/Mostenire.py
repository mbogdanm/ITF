# MOSTENIRE = un fucking concept prin care putem sa oferim
# unor alte clase niste functionalitati deja definite intr-o
# clasa existenta cu scopul de a economis cod

# Pentru ca o clasa sa poate mosteni o alta clas, clasa parinte
# trebuie specificata intre paranteze langa clasa copil in momentul definirii

class Test (): #clasa parinte
    testVariable = 0

class Chef (Test): #clasa copil ce mosteneste parintele
    cutite = 1
    def make_salad(self):
        print('Am facut salata')
    def make_fries(self):
        print('Am facut cartofi prajiti')

class ChefIndian():
    def make_curry(self):
        print('curry')

class JapaneseChef(Chef):
    def make_sushi(self):
        print('Am facut SUSHI! OMG')\

class ItalianChef(ChefIndian,JapaneseChef):
    tava = 1
    def make_pizza(self):
        print('Am facut pizza')

newbe=Chef() #Am definit un obiect instantiat din clasa Chef
newbe.make_fries() #Am apelat metoda make_fries din clasa Chef
print('------------------------------')
nakamoto = JapaneseChef() #initializam un obiect de tip JapaneseChef

print(nakamoto.cutite)
print(nakamoto.make_fries())
print(nakamoto.make_salad())
print(nakamoto.make_sushi())
print(nakamoto.testVariable) # avem acces si la atributul testCariable


chef = Chef()
chef.testVariable

mario = ItalianChef()
mario.make_sushi() #deoarece clasa ItalianChef mostenesete si JapaneseChef, avem acces si
                    #la metoda make_sushi
mario.make_curry() #deoarece clasa ItalianChef mostenesete si ChefIndian, avem acces si
                    #la metoda make_curry
