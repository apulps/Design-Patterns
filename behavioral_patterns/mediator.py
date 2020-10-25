"""
Define an object that encapsulates how a set of objects interact. 
Mediator promotes loose coupling by keeping objects from referring to each other explicitly, and it lets you vary their interaction independently.
"""


class Mediator:
    def notify(self, sender, event):
        raise NotImplementedError("Subclass must override notify()!")


class ConcreteMediator(Mediator):
    def __init__(self, colleageA, colleageB):
        self._colleageA = colleageA
        self._colleageA.set_mediator(self)
        self._colleageB = colleageB
        self._colleageB.set_mediator(self)
    
    def notify(self, sender, event):
        if event == 1:
            self._colleageB.do_something()
        elif event == 4:
            self._colleageA.do_something_else()
            self._colleageB.do_something()


class Colleage:
    def __init__(self, mediator=None):
        self._mediator = mediator
    
    def set_mediator(self, mediator):
        self._mediator = mediator

    def get_mediator(self):
        return self._mediator


class ConcreteColleageA(Colleage):
    def do_something(self):
        self.get_mediator().notify(self, 1)

    def do_something_else(self):
        self.get_mediator().notify(self, 2)


class ConcreteColleageB(Colleage):
    def do_something(self):
        self.get_mediator().notify(self, 3)

    def do_something_else(self):
        self.get_mediator().notify(self, 4)
