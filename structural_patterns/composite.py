"""
Compose objects into tree structures to represent whole-part hierarchies. 
Composite lets clients treat individual objects and compositions of objects uniformly.
"""


class Component:
    def operation(self):
        raise NotImplementedError("Subclass must override operation()!")


class Leaf(Component):
    def operation(self):
        return 1


class Composite(Component):
    def __init__(self):
        self._elements = set()

    def operation(self):
        result = 0

        for element in self._elements:
            result += element.operation()

        return result

    def add_element(self, element):
        self._elements.add(element)
    
    def remove_element(self, element):
        self._elements.discard(element)
