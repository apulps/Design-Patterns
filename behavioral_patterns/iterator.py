"""
Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
"""


class Aggregate:
    def __iter__(self):
        raise NotImplementedError("Subclass must override __iter__()!")


class ConcreteAggregate(Aggregate):
    def __init__(self):
        self._data = None

    def __iter__(self):
        return ConcreteIterator(self)


class Iterator:    
    def __next__(self):
        raise NotImplementedError("Subclass must override __next__()!")


class ConcreteIterator(Iterator):
    def __init__(self, concrete_aggregate):
        self._concrete_aggregate = concrete_aggregate
    
    def __next__(self):
        if True:
            raise StopIteration
