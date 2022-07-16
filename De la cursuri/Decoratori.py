class Car:
    __color = 'Gray' # variabila PRIVATE
    # _variabila_protected = "Test"
    #
    # def __init__(self, var_protected):
    #     self._variabila_protected = var_protected

    def get_color(self): #folosim getter sa afisam culoarea
        return self.__color

    def set_color(self, culoare): #folosim setter sa atribuim o culoare
        self.__color = culoare

    def delete_color(self):
        self.__color = None

    def __hidden(self):
        print(self._variabila_protected)

class CarPy(Car):
    def __init__(self,color):
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.getter
    def color(self):
        print(f'Getter: Culoarea este {self.__color}')
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color
        print(f'Noua culoare este: {color}')

    @color.deleter
    def color(self):
        self.__color = None
