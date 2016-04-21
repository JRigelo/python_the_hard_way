# exercise 42
# Is-A, Has-A, Objects, and Classes

## Class Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    def __init__(self, kind):
        self.kind = kind

## Class Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__("Dog")
        ## Dog has-a attribute name
        self.name = name

    def set_age(self, age):
        if age < 0:
            self.age = 0
        else:
            self.age = age

## Class Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        super(Cat, self).__init__("Cat")
    ## Cat has-a attributte name
        self.name = name
        self.age = None

## Class Person is-a object
class Person(object):
    def __init__(self, name):
        ## Person has-a attribute name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Class Employee is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        ## the attribute name is inherited from Person
        super(Employee, self).__init__(name)
        ## Employee has-a attribute salary
        self.salary = salary

## Class Fish is-a object
class Fish(object):
    def __init__(self, kind):
        self.kind = kind
        self.age = None

## Class Salmon is-a Fish
class Salmon(Fish):
     def __init__(self, name):
         super(Salmon, self).__init__("Salmon")
         self.name = name

## Class Halibut(Fish):
class Halibut(Fish):
    def __init__(self, name):
        super(Halibut, self).__init__("Halibut")
        self.name = name

## rover is-a Dog
rover = Dog("Rover")
rover.set_age(-2)

age = rover.age
print age

rover.set_age(3)
print rover.age

## satan is-a Cat
satan = Cat("Satan")
satan.age = 2

age = satan.age

print age

## mary is-a Person
mary = Person("Mary")

## mary has-a pet satan
mary.pet = satan

## frank is-a Employee and has-a salary of 120000
frank = Employee("Frank", 120000)

## frank has-a pet rover
frank.pet = rover

print frank.pet.age 

## flipper is-a Fish
flipper = Fish("Salmon")

## crouse is-a Salmon
crouse = Salmon("Crouse")

## harry is-a Halibut
harry = Halibut("Harry")
