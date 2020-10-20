"""
Convert the interface of a class into another interface clients expect. Adapter lets classes work together that couldn't otherwise because of incompatible interfaces.
"""


class Target:
    def request(self):
        raise NotImplementedError("Subclass must override request()!")


class Adapter(Target):
    def __init__(self):
        self._adaptee = Adaptee()

    def request(self):
        return self._adaptee.specific_request()


class Adaptee:
    def specific_request(self):
        return 1
