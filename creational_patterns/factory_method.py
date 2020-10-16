"""
Define an interface to create an object, but let the subclasses decide the class to instantiate. 
The instantiation is delegated to the subclasses.
"""


class Product:
    def do_something(self):
        raise NotImplementedError("Subclass must override do_something()!")

    def do_something_else(self):
        raise NotImplementedError("Subclass must override do_something_else()!")


class ConcreteProduct(Product):
    def do_something(self):
        return 1

    def do_something_else(self):
        return 2


class Creator:
    def factory_method(self):
        raise NotImplementedError("Subclass must override factory_method()!")


class ConcreteCreator(Creator):
    def factory_method(self):
        return ConcreteProduct()
