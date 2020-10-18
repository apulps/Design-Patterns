"""
Provide an interface for creating families of related or dependent objects without specifying their concrete classes.
"""


class AbstractProductA:
    def do_something(self):
        raise NotImplementedError("Subclass must override do_something()!")

    def do_something_else(self):
        raise NotImplementedError("Subclass must override do_something_else()!")


class ConcreteProductA1(AbstractProductA):
    def do_something(self):
        return 1

    def do_something_else(self):
        return 2


class ConcreteProductA2(AbstractProductA):
    def do_something(self):
        return 3

    def do_something_else(self):
        return 4



class AbstractProductB:
    def do_something(self):
        raise NotImplementedError("Subclass must override do_something()!")

    def do_something_else(self):
        raise NotImplementedError("Subclass must override do_something_else()!")


class ConcreteProductB1(AbstractProductB):
    def do_something(self):
        return 5

    def do_something_else(self):
        return 6


class ConcreteProductB2(AbstractProductB):
    def do_something(self):
        return 7

    def do_something_else(self):
        return 8
    


class AbstractFactory:
    def make_productA(self):
        raise NotImplementedError("Subclass must override make_productA()!")

    def make_productB(self):
        raise NotImplementedError("Subclass must override make_productB()!")


class ConcreteFactory1(AbstractFactory):
    def make_productA(self):
        return ConcreteProductA1()

    def make_productB(self):
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    def make_productA(self):
        return ConcreteProductA2()

    def make_productB(self):
        return ConcreteProductB2()
