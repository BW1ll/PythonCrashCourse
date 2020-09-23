# Python Crash Course - Chapter 9 Summary

****main topics****

```Python
# 1) top 7 most import topics in chapter 9
# 2) top 5 most import
# 3) top 3 most import

top_7 = ['Method vs Function', '__init__()', 'special methods', 'styling Classes', 'inheritance',
         'importing', 'Python Standard Library']
top_5 = ['__init__()','special methods','styling Classes', 'inheritance', 'importing']
top_3 = ['special methods', 'styling Classes', 'importing']
```

## Classes

***Class*** = represent real world things, objects are created based on these things

- Class: define the general behavior of the object and are created similarly to the "define functions" method (def)
- Method: method is like a Python function, but it must be called on an object.
- instance: object created from a class
- Attribute: Python variable that belongs to a class rather than a particular object.

### Start by defining a class with the Python key-word "class"

```Python
class NameOfClass: # styling class name should be Capitalized and CamelCase
    pass    # classes cannot be created without at least one line code in them
```

### Write a doc sting that summarize what the class does

```Python
'''This is an example of a doc string'''
"""This is also and example of a doc string"""
```

### Initialize Parameters

The ``__init__``() method is a special method Python automatically runs when creating an instance of a class.  
It is often called a constructor in other languages.  
In Python, methods that start and end with double underscores hold special meaning, and are often referred to as "Dunder Methods"

```Python
def __init__(self, parameter1, parameter2):
```

### Assign class variables

Any variable that begins with self is available to every Method in the class

```Python
self.parameter1 = parameter1
self.parameter2 = parameter2
```

"self.parameter1 = parameter1" takes the value associated with the parameter parameter1 and assigns it to the variable parameter1.  
The variable parameter1 is then attached to the instance that is being created.  
self is passed automatically  
  
### Define any methods for the class

```Python3
def method1(self):
    pass

def method2(self):
    pass
```

### Create an instance

Create an instance/s of the class and pass required parameters

```Python
instance1 = NameOfClass(parameter1, parameter2)
instance2 = NameOfClass(parameter1, parameter2)
```

### Calling methods of an instance

```Python
instance1.method1()
instance1.method2()

instance2.method1()
instance2.method2()
```

### example class

```Python
class NameOfClass:
    '''This is an example of a doc string'''

    def __init__(self, parameter1, parameter2):
        '''initialize parameters'''
        self.parameter1 = parameter1
        self.parameter2 = parameter2

    def method1(self):
        '''Document Method here'''
        pass

    def method2(self):
        '''Document Method here'''
        pass
```

### class Dog from PCC

```Python
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
```

out put:

> My dog's name is Willie.
> My dog is 6 years old.
> Willie is now sitting.
> Your dog's name is Lucy.
> Your dog is 3 years old.
> Lucy is now sitting.

### Working with classes and instances

#### Setting a default value for an Attribute

```Python
class NameOfClass:
    '''This is an example of a doc string'''

    def __init__(self, parameter1, parameter2):
        '''initialize parameters'''
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = 0 # setting default value

    def method1(self):
        '''Document Method'''
        pass

    def method2(self):
        '''Document Method'''
        pass
```

#### Modifying Attribute Values  

##### Directly

```Python
instance1 = NameOfClass(parameter1, parameter2)

instance1.method1()

example_string = f'{instance1.parameter1} will print parameter1 in a string'
instance1.parameter1 = 'changed value of parameter1'
```

##### Through a Method

```Python
def update_parameter3(self, new_value):
    '''Example on how to create method to update attribute'''
    self.parameter3 = new_value
    print(self.parameter3)
# method output would print the updated value of self.parameter3
```

##### Incrementing Value through a Method

```Python
def update_parameter3(self, new_value):
    '''Example on how to create method to update attribute'''
    self.parameter3 += new_value
# method output would print the updated value of self.parameter3
```

## Inheritance

You can create specialized subclass of a class.  Whe you create a subclass,  
the subclass becomes the child class and the one it inherits form becomes the parent.

### The ``__init__``() Method for a child class

```Python
class Subclass(NameOfClass):
    '''Document Subclass '''

    def __init__(self, parameter1, parameter2):
        '''Initialize the attributes of thee parent class'''
        super().__init__(self, parameter1, parameter2)
        # super() is a special function that allows you to call a method from the parent class
```

The super() method is wat allows the child class to inherit all of the attributes and methods  
of the parent class  
  
### Defining Attributes and Methods for the Child Class

```Python
class Subclass(NameOfClass):
    '''Document Subclass '''

    def __init__(self, parameter1, parameter2):
        '''
        Initialize the attributes of thee parent class
        Then initialize attributes specific to the subclass
        '''
        super().__init__(self, parameter1, parameter2)
        sell.parameter4 = parameter4

    def subclassMethod(self):
        pass

```

## Instances as Attributes

```Python
class Car:
    --snip--    #sniped for space

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()    # Making an instance and attribute

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```

## Importing

### Importing Classes

```Python
# Using the Car, Battery, and ElectricCar classes above,
# all saved in one file(also called a module) called car.py

from car import Car # importing one class from module
my_mustang = Car('ford', 'mustang', 2019)

from car import Car, ElectricCar    # importing multiple classes from module
my_mustang = Car('ford', 'mustang', 2019)
my_tesla = ElectricCar('tesla', 'model s', 2019)

import car  # imports the entire module
my_mustang = car.Car('ford', 'mustang', 2019)
my_tesla = car.ElectricCar('tesla', 'model s', 2019)

from car import *  # imports all classes form module, not recommended.
# Being able to read the import statement to see what classes you are using
# is helpful, not knowing can lead to naming conflict within your program
# or other unforeseen issues
```

### Importing Module into a Module

```Python
# module battery
class Battery:
    --snip--

# Module car:
from battery import Battery

class Car:
    --snip--

class ElectricCar(Car):
    --snip--

# Project module:
from car import Car, ElectricCar

my_mustang = car.Car('ford', 'mustang', 2019)
my_tesla = car.ElectricCar('tesla', 'model s', 2019)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```

### Using Aliases

```Python
from car import Car as C
from car import ElectricCar as EC

my_mustang = C('ford', 'mustang', 2019)
my_tesla = EC('tesla', 'model s', 2019)
```

## The Python Standard Library

***Python Standard Library*** = set of modules included with every Python installation

<https://docs.python.org/3/library/>
