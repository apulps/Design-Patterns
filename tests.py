import unittest

from creational_patterns.singleton import MyClass as MyClassSingleton
from creational_patterns.prototype import Client as ClientPrototype, Prototype
from creational_patterns.factory_method import Product, ConcreteProduct, Creator, ConcreteCreator
from creational_patterns.abstract_factory import (
    AbstractFactory, 
    ConcreteFactory1, 
    ConcreteFactory2, 
    AbstractProductA, 
    AbstractProductB, 
    ConcreteProductA1,
    ConcreteProductB1,
    ConcreteProductA2,
    ConcreteProductB2
)
from creational_patterns.builder import Director, Builder, ConcreteBuilder, Product as ProductB

from structural_patterns.adapter import Target, Adapter, Adaptee
from structural_patterns.facade import Facade, Class1, Class2, Class3
from structural_patterns.decorator import Component, ConcreteComponent, Decorator, ConcreteDecoratorA, ConcreteDecoratorB
from structural_patterns.composite import Component as ComponentB, Leaf, Composite
from structural_patterns.bridge import Abstraction, ExtendedAbstraction, Implementation, ConcreteImplementationA, ConcreteImplementationB
from structural_patterns.proxy import Subject, RealSubject, Proxy

from behavioral_patterns.iterator import Aggregate, ConcreteAggregate, Iterator, ConcreteIterator
from behavioral_patterns.command import Invoker, Command, Command1, Reciever
from behavioral_patterns.observer import Subject as SubjectB, ConcreteSubject, Observer, ConcreteObserver
from behavioral_patterns.mediator import Mediator, ConcreteMediator, Colleage, ConcreteColleageA, ConcreteColleageB
from behavioral_patterns.state import Context, State, ConcreteStateA, ConcreteStateB
from behavioral_patterns.strategy import Context as ContextB, Strategy, ConcreteStrategyA, ConcreteStrategyB
from behavioral_patterns.template_method import AbstractClass, ConcreteClass1, ConcreteClass2



class TestCreationalPatterns(unittest.TestCase):
    def test_singleton(self):
        A = MyClassSingleton()
        B = MyClassSingleton()
        self.assertIs(A, B)


    def test_prototype(self):
        x_value, y_value = 10, 20
        c = ClientPrototype(5, x_value, y_value)
        even = c.method(1) # position 1, 2nd value -> even
        odd = c.method(2) # position 2, 3rd value -> odd
        self.assertEqual(even.x, 9)
        self.assertEqual(even.y, y_value)
        self.assertEqual(odd.x, x_value)
        self.assertEqual(odd.y, 8)

        self.assertRaises(NotImplementedError, Prototype(0, 0).clone) # test abstract method


    def test_factory_method(self):
        concrete_product = ConcreteCreator().factory_method()
        
        self.assertIsInstance(concrete_product, ConcreteProduct) # test type of object
        self.assertEqual(concrete_product.do_something(), 1) # test implemented method
        self.assertEqual(concrete_product.do_something_else(), 2) # test implemented method
        
        self.assertRaises(NotImplementedError, Product().do_something) # test abstract method
        self.assertRaises(NotImplementedError, Product().do_something_else) # test abstract method

        self.assertRaises(NotImplementedError, Creator().factory_method) # test abstract method

    
    def test_abstract_factory(self):
        self.assertRaises(NotImplementedError, AbstractFactory().make_productA) # test abstract method
        self.assertRaises(NotImplementedError, AbstractFactory().make_productB) # test abstract method
        
        self.assertRaises(NotImplementedError, AbstractProductA().do_something) # test abstract method
        self.assertRaises(NotImplementedError, AbstractProductA().do_something_else) # test abstract method

        self.assertRaises(NotImplementedError, AbstractProductB().do_something) # test abstract method
        self.assertRaises(NotImplementedError, AbstractProductB().do_something_else) # test abstract method

        concrete_factory1 = ConcreteFactory1()
        concrete_productA1 = concrete_factory1.make_productA()
        concrete_productB1 = concrete_factory1.make_productB()

        self.assertIsInstance(concrete_productA1, ConcreteProductA1)
        self.assertIsInstance(concrete_productB1, ConcreteProductB1)
        self.assertEqual(concrete_productA1.do_something(), 1)
        self.assertEqual(concrete_productA1.do_something_else(), 2)
        self.assertEqual(concrete_productB1.do_something(), 5)
        self.assertEqual(concrete_productB1.do_something_else(), 6)

        concrete_factory2 = ConcreteFactory2()
        concrete_productA2 = concrete_factory2.make_productA()
        concrete_productB2 = concrete_factory2.make_productB()

        self.assertIsInstance(concrete_productA2, ConcreteProductA2)
        self.assertIsInstance(concrete_productB2, ConcreteProductB2)
        self.assertEqual(concrete_productA2.do_something(), 3)
        self.assertEqual(concrete_productA2.do_something_else(), 4)
        self.assertEqual(concrete_productB2.do_something(), 7)
        self.assertEqual(concrete_productB2.do_something_else(), 8)
    

    def test_builder(self):
        self.assertRaises(NotImplementedError, Builder().build_part_a) # test abstract method
        self.assertRaises(NotImplementedError, Builder().build_part_b) # test abstract method

        concrete_builder = ConcreteBuilder()
        director = Director()
        director.build(concrete_builder)
        product = concrete_builder.get_product()
        
        self.assertEqual(product.feature_1, 1)
        self.assertEqual(product.feature_2, 2)



class TestStructuralPatterns(unittest.TestCase):
    def test_adapter(self):
        self.assertRaises(NotImplementedError, Target().request) # test abstract method

        adapter = Adapter()
        
        self.assertEqual(adapter.request(), 1)
    

    def test_facade(self):
        self.assertRaises(NotImplementedError, Class1().method_1) # test abstract method

        self.assertEqual(Class1().method_2(), 2)
        self.assertEqual(Class2().method_1(), 1)
        self.assertEqual(Class2().method_2(), 2)
        self.assertEqual(Class3().method_3(), 3)

        facade = Facade()
        
        self.assertEqual(facade.operation(), 6)

    
    def test_decorator(self):
        self.assertRaises(NotImplementedError, Component().operation) # test abstract method

        concrete_component = ConcreteComponent()

        self.assertEqual(concrete_component.operation(), 1)

        decorator = Decorator(concrete_component)

        self.assertEqual(decorator.operation(), 1)

        concrete_decoratorA = ConcreteDecoratorA(concrete_component)
        concrete_decoratorB = ConcreteDecoratorB(concrete_component)

        self.assertEqual(concrete_decoratorA.operation(), 2)
        self.assertEqual(concrete_decoratorB.operation(), 4)
        self.assertEqual(concrete_decoratorB.other_operation(), 3)
    

    def test_composite(self):
        self.assertRaises(NotImplementedError, ComponentB().operation) # test abstract method
        
        leaf_1 = Leaf()

        self.assertEqual(leaf_1.operation(), 1)

        leaf_2 = Leaf()
        leaf_3 = Leaf()
        leaf_4 = Leaf()
        composite = Composite()

        composite.add_element(leaf_1)
        composite.add_element(leaf_2)
        composite.add_element(leaf_3)
        composite.add_element(leaf_4)

        self.assertEqual(len(composite._elements), 4)

        composite.remove_element(leaf_2)
        composite.remove_element(leaf_4)
        
        self.assertEqual(len(composite._elements), 2)

        self.assertEqual(composite.operation(), 2)

    
    def test_bridge(self):
        self.assertRaises(NotImplementedError, Implementation().implemented_operation) # test abstract method

        concrete_implementationA = ConcreteImplementationA()
        concrete_implementationB = ConcreteImplementationB()

        self.assertEqual(concrete_implementationA.implemented_operation(), 2)
        self.assertEqual(concrete_implementationB.implemented_operation(), 3)

        abstractionA = Abstraction(concrete_implementationA)
        abstractionB = Abstraction(concrete_implementationB)

        self.assertEqual(abstractionA.operation(), f'Result from Abstraction: 2')
        self.assertEqual(abstractionB.operation(), f'Result from Abstraction: 3')

        extended_abstractionA = ExtendedAbstraction(concrete_implementationA)
        extended_abstractionB = ExtendedAbstraction(concrete_implementationB)

        self.assertEqual(extended_abstractionA.operation(), f'Result from ExtendedAbstraction: 2')
        self.assertEqual(extended_abstractionB.operation(), f'Result from ExtendedAbstraction: 3')

    
    def test_proxy(self):
        self.assertRaises(NotImplementedError, Subject().operation) # test abstract method

        real_subject = RealSubject()

        self.assertEqual(real_subject.operation(), 1)

        proxy = Proxy(real_subject)

        self.assertEqual(proxy.operation(), 1)



class TestBehavioralPatterns(unittest.TestCase):
    def test_iterator(self):
        self.assertRaises(NotImplementedError, Aggregate().__iter__) # test abstract method

        self.assertRaises(NotImplementedError, Iterator().__next__) # test abstract method

        concrete_aggregate = ConcreteAggregate()
        concrete_iterator = iter(concrete_aggregate)

        self.assertRaises(StopIteration, concrete_iterator.__next__)
    

    def test_command(self):
        self.assertRaises(NotImplementedError, Command().execute) # test abstract method
        
        reciever = Reciever()
        command1 = Command1(reciever)
        invoker = Invoker()
        invoker.store_command(command1)
        
        self.assertEqual(invoker.execute_commands(), 1)

    
    def test_observer(self):
        self.assertRaises(NotImplementedError, Observer().update) # test abstract method
        
        concrete_subject = ConcreteSubject()
        concrete_observer = ConcreteObserver(concrete_subject)
        concrete_subject.atach(concrete_observer)

        self.assertEqual(concrete_subject.get_state(), None)
        self.assertEqual(concrete_observer._observer_state, 10)

        concrete_subject.set_state(5)

        self.assertEqual(concrete_subject.get_state(), 5)
        self.assertEqual(concrete_observer._observer_state, 5)

        concrete_subject.detach(concrete_observer)
    

    def test_mediator(self):
        self.assertRaises(NotImplementedError, Mediator().notify, None, None) # test abstract method

        colleageA = ConcreteColleageA()
        colleageB = ConcreteColleageB()

        self.assertEqual(colleageA.get_mediator(), None)
        self.assertEqual(colleageB.get_mediator(), None)

        ConcreteMediator(colleageA, colleageB)

        colleageA.do_something()
        colleageB.do_something_else()

    
    def test_state(self):
        self.assertRaises(NotImplementedError, State().handle) # test abstract method

        context = Context(ConcreteStateA())

        self.assertIsInstance(context.get_state(), ConcreteStateA)

        context.request()

        self.assertIsInstance(context.get_state(), ConcreteStateB)

        context.request()

        self.assertIsInstance(context.get_state(), ConcreteStateA)

    
    def test_strategy(self):
        self.assertRaises(NotImplementedError, Strategy().algorithm_interface, None) # test abstract method

        data = [3,2,1,5,6]

        concrete_strategyA = ConcreteStrategyA()
        concrete_strategyB = ConcreteStrategyB()

        context = ContextB(concrete_strategyA)

        self.assertEqual(context.context_interface(data), [1,2,3,5,6])

        context = ContextB(concrete_strategyB)

        self.assertEqual(context.context_interface(data), [6,5,3,2,1])
    

    def test_template_method(self):
        self.assertRaises(NotImplementedError, AbstractClass().required_operation1) # test abstract method
        self.assertRaises(NotImplementedError, AbstractClass().required_operation2) # test abstract method

        concrete_class1 = ConcreteClass1()

        self.assertEqual(concrete_class1.template_method(), 3)
        
        concrete_class2 = ConcreteClass2()

        self.assertEqual(concrete_class2.template_method(), 17)

        concrete_class2.hook2()



if __name__ == "__main__":
    unittest.main()
