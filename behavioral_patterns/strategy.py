"""
Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from the clients that use it.
"""


class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def context_interface(self, data):
        return self._strategy.algorithm_interface(data)


class Strategy:
    def algorithm_interface(self, data):
        raise NotImplementedError("Subclass must override context_algorithm()!")


class ConcreteStrategyA(Strategy):
    def algorithm_interface(self, data):
        return [e for e in sorted(data)]


class ConcreteStrategyB(Strategy):
    def algorithm_interface(self, data):
        return [e for e in reversed(sorted(data))]
