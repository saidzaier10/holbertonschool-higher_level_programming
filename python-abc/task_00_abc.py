from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"

        def shape_info(shape):
            print("Area:", shape.area())
            print("Perimeter:", shape.perimeter())
