"""
INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură
"""


class FormaGeometrica: #clasa parinte care contine atributul latura si constructorul pentru aceasta
    latura = None

    def __init__(self, latura):
        self.latura = latura


class Patrat(FormaGeometrica):

    def construieste_cerc(self):
        print(f'Patratul are latura: {self.latura}')


patrat1 = Patrat(7)
forma = FormaGeometrica()
