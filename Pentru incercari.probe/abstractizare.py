from abc import ABC, abstractmethod

class Animal (ABC):

    @abstractmethod
    def sound(self):
        raise NotImplementedError

    @abstractmethod
    def sleep(self):
        # raise NotImplementedError
        pass

class Dog (Animal):
    def sound (self):
        print('Woof, woof!')

    # def sleep(self):
    #     print('I also sleep')

caine = Dog()
caine.sound()