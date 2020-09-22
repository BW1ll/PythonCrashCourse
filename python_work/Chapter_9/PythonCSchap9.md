# Python Crash Course - Chapter 9 Summary

****main topics****

```Python
# 1) top 7 most import topics in chapter 9
# 2) top 5 most import
# 3) top 3 most import

top_7 = ['Method', '__init__()','instances','attributes', 'child/parent class', 'doc string', 'importing PSL']
top_5 = ['__init__()','instances','attributes', 'child/parent class', 'importing PSL']
top_3 = ['__init__()', 'instances', 'importing PSL']
```

## Classes

***Classes*** = represent real world things, objects are created based on these things

- classes define the general behavior of the object and are created similarly to the "define functions" method (def)
- Method: method is like a Python function, but it must be called on an object.
- instance: object created from a class
- Attribute: Python variable that belongs to a class rather than a particular object.

start by defining a class with the Python key-word "class"

```Python
class NameOfClass:
    pass
```

write a doc sting that summarize what the class does

```Python
'''This is an example of a doc string'''
```

the __init__() method is a special method Python automatically runs when creating an instance of a class.  
it is often call a constructor in other languages

```Python
def __init__(self, parameter1, parameter2):
```

Assign any class variables.  Any variable that begins with self is available to every Method in the class

```Python
self.parameter1 = parameter1
self.parameter2 = parameter2
```

self.parameter1 = parameter1 takes the value associated with the parameter parameter1 and assigns it to the variable parameter1.  
The variable parameter1 is then attached to the instance that is being created.  
self is passed automatically
