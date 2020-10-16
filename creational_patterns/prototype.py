"""
Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.

Python's copy() makes a shallow copy. Constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
Python's deepcopy() makes a deep copy. Constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.

We can use deepcopy() for this design pattern.
"""


class Prototype:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        raise NotImplementedError("Subclass must override clone()!")


class ConcretePrototypeA(Prototype):
    """
    Odds.
    """
    def clone(self):
        p = ConcretePrototypeA(8, 8)
        p.x = self.x
        return p


class ConcretePrototypeB(Prototype):
    """
    Evens.
    """
    def clone(self):
        p = ConcretePrototypeB(9, 9)
        p.y = self.y
        return p
        

class Client:
    def __init__(self, amount, x_value, y_value):
        self.z = [ConcretePrototypeA(x_value, y_value) if i % 2 == 0 else ConcretePrototypeB(x_value, y_value) for i in range(amount)]

    def method(self, n):
        return self.z[n].clone()
