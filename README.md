# Design-Patterns

[![Build Status](https://travis-ci.org/apulps/Design-Patterns.svg?branch=main)](https://travis-ci.org/apulps/Design-Patterns)
[![codecov](https://codecov.io/gh/apulps/Design-Patterns/branch/main/graph/badge.svg?token=GNVMHFNXPU)](https://codecov.io/gh/apulps/Design-Patterns)

## Creational patterns

### Singleton
Ensures that a class has only one instance and provides a global point of access to it.

![Singleton](uml/singleton.png "Singleton")

### Prototype
Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.

![Prototype](uml/prototype.png "Prototype")

### Factory Method
Define an interface to create an object, but let the subclasses decide the class to instantiate. The instantiation is delegated to the subclasses.

![Factory Method](uml/factory_method.png "Factory Method")

### Abstract Factory
Provide an interface for creating families of related or dependent objects without specifying their concrete classes.

![Abstract Factory](uml/abstract_factory.png "Abstract Factory")

### Builder
Separate the construction of a complex object from its representation so that the same construction process can create different representations.

![Builder](uml/builder.png "Builder")

<!--
### Object Pool
-->


## Structural patterns

### Adapter
Convert the interface of a class into another interface clients expect. Adapter lets classes work together that couldn't otherwise because of incompatible interfaces.

![Adapter](uml/adapter.png "Adapter")

### Facade
Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.

![Facade](uml/facade.png "Facade")

### Decorator
Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.

![Decorator](uml/decorator.png "Decorator")

### Composite
Compose objects into tree structures to represent whole-part hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.

![Composite](uml/composite.png "Composite")

### Bridge
Decouple an abstraction from its implementation so that the two can vary independently.

![Bridge](uml/bridge.png "Bridge")

### Proxy
Provide a surrogate or placeholder for another object to control access to it.

![Proxy](uml/proxy.png "Proxy")

<!--
### Flyweight
### Private Class Data
-->


## Behavioral patterns

### Iterator
Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

![Iterator](uml/iterator.png "Iterator")

### Command
Encapsulate a request as an object, thereby letting you parametrize clients with different requests, queue or log requests, and support undoable operations.

![Command](uml/command.png "Command")

### Observer
Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

![Observer](uml/observer.png "Observer")

### Mediator
Define an object that encapsulates how a set of objects interact. Mediator promotes loose coupling by keeping objects from referring to each other explicitly, and it lets you vary their interaction independently.

![Mediator](uml/mediator.png "Mediator")

### State
Allow an object to alter its behavior when its internal state changes. The object will appear to change its class.

![State](uml/state.png "State")

### Strategy
Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from the clients that use it.

![Strategy](uml/strategy.png "Strategy")

### Template method
Define the skeleton of an algorithm in an operation, deferring some steps to client subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.

![Template method](uml/template_method.png "Template method")

<!--
### Chain of responsibility
### Memento
### Null Object
### Visitor
-->