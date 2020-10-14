import unittest
from creational_patterns.singleton import MyClass


class TestCreationalPatterns(unittest.TestCase):
    def test_singleton(self):
        A = MyClass()
        B = MyClass()
        assert A is B



if __name__ == "__main__":
    unittest.main()