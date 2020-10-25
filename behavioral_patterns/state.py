"""
Allow an object to alter its behavior when its internal state changes. The object will appear to change its class.
"""


class Context:
    def __init__(self, state):
        self.transition_to(state)

    def request(self):
        self.get_state().handle()
    
    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state

    def transition_to(self, state):
        self.set_state(state)
        self.get_state().set_context(self)


class State:
    def set_context(self, context):
        self._context = context
    
    def get_context(self):
        return self._context
    
    def handle(self):
        raise NotImplementedError("Subclass must override handle()!")


class ConcreteStateA(State):
    def handle(self):
        self.get_context().transition_to(ConcreteStateB())


class ConcreteStateB(State):
    def handle(self):
        self.get_context().transition_to(ConcreteStateA())
