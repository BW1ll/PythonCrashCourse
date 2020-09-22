# Python Crash Course - Chapter 9 Summary

****main topics****

```Python
# 1) top 7 most import topics in chapter 9
# 2) top 5 most import
# 3) top 3 most import

top_7 = ['Method vs Function', '__init__()', 'special methods', 'styling Classes', 'inheritance', 'importing', 'Python Standard Library']
top_5 = ['__init__()','special methods','styling Classes', 'inheritance', 'importing']
top_3 = ['special methods', 'styling Classes', 'importing']
```

## Classes

***Class*** = represent real world things, objects are created based on these things

- Class: define the general behavior of the object and are created similarly to the "define functions" method (def)
- Method: method is like a Python function, but it must be called on an object.
- instance: object created from a class
- Attribute: Python variable that belongs to a class rather than a particular object.

Start by defining a class with the Python key-word "class"

```Python
class NameOfClass: # styling class name should be Capitalized and CamelCase
    pass    # classes cannot be created without at least one line code in them
```

Write a doc sting that summarize what the class does.

```Python
'''This is an example of a doc string'''
```

The __init__() method is a special method Python automatically runs when creating an instance of a class.  
It is often called a constructor in other languages.

```Python
def __init__(self, parameter1, parameter2):
```

Assign any class variables.  Any variable that begins with self is available to every Method in the class

```Python
self.parameter1 = parameter1
self.parameter2 = parameter2
```

"self.parameter1 = parameter1" takes the value associated with the parameter parameter1 and assigns it to the variable parameter1.  
The variable parameter1 is then attached to the instance that is being created.  
self is passed automatically  
  
Define any methods for the class

```Python3
def method1(self):
    pass

def method2(self):
    pass
```

Create an instance/s of the class and pass required parameters

```Python
instance1 = NameOfClass(parameter1, parameter2)
instance2 = NameOfClass(parameter1, parameter2)
```

Calling methods of an instance

```Python
instance1.method1()
instance1.method2()

instance2.method1()
instance2.method2()
```

example class

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

class Dog from PCC

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

- "My dog's name is Willie."
- "My dog is 6 years old."
- "Willie is now sitting."
- "Your dog's name is Lucy."
- "Your dog is 3 years old."
- "Lucy is now sitting."

### Working with classes and instances

Setting a default value for an Attribute

```Python
class NameOfClass:
    '''This is an example of a doc string'''

    def __init__(self, parameter1, parameter2):
        '''initialize parameters'''
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = 0

    def method1(self):
        '''Document Method'''
        pass

    def method2(self):
        '''Document Method'''
        pass
```

Modifying Attribute Values  
Directly

```Python
instance1 = NameOfClass(parameter1, parameter2)

instance1.method1()

example_string = f'{instance1.parameter1} will print parameter1 in a string'
instance1.parameter1 = 'changed value of parameter1'
```

Through a Method

```Python
def update_parameter3(self, new_value):
    '''Example on how to create method to update attribute'''
    self.parameter3 = new_value
    print(self.parameter3)
# method output would print the updated value of self.parameter3
```

Incrementing Value through a Method

```Python
def update_parameter3(self, new_value):
    '''Example on how to create method to update attribute'''
    self.parameter3 += new_value
# method output would print the updated value of self.parameter3
```

## Inheritance
