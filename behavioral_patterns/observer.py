"""
Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
"""


class Subject:
    def __init__(self):
        self._observers = []
        self._subject_state = None

    def atach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()


class ConcreteSubject(Subject):
    def set_state(self, new_state):
        self._subject_state = new_state
        self.notify()
    
    def get_state(self):
        return self._subject_state


class Observer:
    def __init__(self):
        self._subject = None
        self._observer_state = None

    def update(self):
        raise NotImplementedError("Subclass must override update()!")


class ConcreteObserver(Observer):
    def __init__(self, subject):
        self._subject = subject
        self._observer_state = 10

    def update(self):
        self._observer_state = self._subject.get_state()
