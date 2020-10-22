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

        decorator = Decorator()

        self.assertEqual(decorator.operation(), 1)

        concrete_decoratorA = ConcreteDecoratorA()
        concrete_decoratorB = ConcreteDecoratorB()

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



if __name__ == "__main__":
    unittest.main()
