"""
Provide a surrogate or placeholder for another object to control access to it.
"""


class Subject:
    def operation(self):
        raise NotImplementedError("Subclass must override operation()!")


class RealSubject(Subject):
    def operation(self):
        return 1


class Proxy(Subject):
    def __init__(self, wrapee):
        self._wrapee = wrapee

    def operation(self):
        return self._wrapee.operation()
