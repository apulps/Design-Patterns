import unittest

from creational_patterns.singleton import MyClass as MyClassSingleton
from creational_patterns.prototype import Client as ClientPrototype, Prototype
from creational_patterns.factory_method import Product, ConcreteProduct, Creator, ConcreteCreator


class TestCreationalPatterns(unittest.TestCase):
    def test_singleton(self):
        A = MyClassSingleton()
        B = MyClassSingleton()
        assert A is B


    def test_prototype(self):
        x_value, y_value = 10, 20
        c = ClientPrototype(5, x_value, y_value)
        even = c.method(1) # position 1, 2nd value -> even
        odd = c.method(2) # position 2, 3rd value -> odd
        self.assertEqual(even.x, 9)
        self.assertEqual(even.y, y_value)
        self.assertEqual(odd.x, x_value)
        self.assertEqual(odd.y, 8)

        self.assertRaises(NotImplementedError, Prototype(0, 0).clone) # test abstract method


    def test_factory_method(self):
        concrete_product = ConcreteCreator().factory_method()
        
        self.assertIsInstance(concrete_product, ConcreteProduct) # test type of object
        self.assertEqual(concrete_product.do_something(), 1) # test implemented method
        self.assertEqual(concrete_product.do_something_else(), 2) # test implemented method
        
        self.assertRaises(NotImplementedError, Product().do_something) # test abstract method
        self.assertRaises(NotImplementedError, Product().do_something_else) # test abstract method

        self.assertRaises(NotImplementedError, Creator().factory_method) # test abstract method




if __name__ == "__main__":
    unittest.main()
