import unittest

from creational_patterns.singleton import MyClass as MyClassSingleton
from creational_patterns.prototype import Client as ClientPrototype, Prototype


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



if __name__ == "__main__":
    unittest.main()
