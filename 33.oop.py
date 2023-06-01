# Object-oriented programming is a programming paradigm that revolves around the concept of objects. 
# In OOP, an object is an instance of a class, which is a blueprint for creating objects. 
# Each object has its own set of properties and methods.
# To define a class in Python, you use the class keyword, followed by the name of the class.
# Here's an example:

class Person:
    pass

# This creates a class called Person. The pass statement is a placeholder that tells Python to do nothing.
# Now that we have a class, we can create objects from it.
# To create an object, you use the name of the class followed by parentheses.
# Here's an example:

person = Person()

# This creates an object called person from the Person class. However, this object doesn't have any properties or methods yet.
# To add properties to a class, you define them in the class using the self parameter. 
# self refers to the object itself. Here's an example:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# This adds a constructor method to the Person class.
# This adds a constructor method to the Person class.
# Inside the constructor method, we use the self parameter to set the name and age properties of the object.
# Now, when we create a Person object, we can pass in values for the name and age properties.
# Here's an example:

person = Person("Alice", 25)

# This creates a Person object called person with a name property of "Alice" and an age property of 25.
# To add methods to a class, you define them in the class using the self parameter.
# Here's an example:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# This adds a method called say_hello to the Person class. The method takes no parameters, but it uses the self parameter to access the name and age properties of the object.
# Now, when we call the say_hello method on a Person object, it will print out a greeting with the name and age of the object.
# Here's an example:

person = Person("Alice", 25)
person.say_hello()  # Output: Hello, my name is Alice andI am 25 years old.

# That's a brief introduction to OOP in Python.
# I hope it helps you get started! Let me know if you have any further questions.


# in class another class can inherited the property

class animal:
    alive = True
    def eat(self):
        print("it is eating")

class rabbit(animal):
    def hop(self):
        print("rabbit is hopping")

