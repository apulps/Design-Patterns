"""
Separate the construction of a complex object from its representation so that the same construction process can create different representations.
"""


class Director:
    def build(self, builder):
        builder.build_part_a()
        builder.build_part_b()


class Builder:
    def __init__(self):
        self._product_under_construction = Product()

    def build_part_a(self):
        raise NotImplementedError("Subclass must override build_part_a()!")

    def build_part_b(self):
        raise NotImplementedError("Subclass must override build_part_b()!")

    def get_product(self):
        out = self._product_under_construction
        self._product_under_construction = Product()
        return out  


class ConcreteBuilder(Builder):
    def build_part_a(self):
        self._product_under_construction.add_feature_1()

    def build_part_b(self):
        self._product_under_construction.add_feature_2()


class Product:
    def __init__(self):
        self.feature_1 = None
        self.feature_2 = None

    def add_feature_1(self):
        self.feature_1 = 1

    def add_feature_2(self):
        self.feature_2 = 2
