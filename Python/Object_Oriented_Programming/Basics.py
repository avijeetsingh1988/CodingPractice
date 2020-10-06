"""Object Oriented programming advantages:
a) Development is Faster and cheaper.
b) Higher Quality Software 

Examples of OOP Language: (Imperative Programming Languages)
C, C++, Java, GO, Ruby, Python


"An example of a class is the class Dog. Don't think of it as a specific dog, or your own dog. We're describing what a dog is 
and can do, in general. Dogs usually have a name and age; these are instance attributes. Dogs can also bark; this is a method.

When you talk about a specific dog, you would have an object in programming: an object is an instantiation of a class. This 
is the basic principle on which object-oriented programming is based. So my dog Ozzy, for example, belongs to the class Dog.His attributes are name = 'Ozzy' and age = '2'. A different dog will have different attributes." - DataCamp"""

class dog:                             # This is how you define a class#
   legs=4                              # This is called the class variable or the static varibale and is constant for all objects.
   def __init__(self,name,age):        # __init__ is to initialize the variables. It is also called a constructor.
      self.name=name                   # self is referred to the object of class 'dog' and 'name' & 'age' are attributes.
      self.age=age                     # These variables are called instance varibales
    
   def bark(self):
      print('BOW')                     # This is a function but in a class this is called as its method.

bruno = dog('bruno',2)                 # This statement classifies 'bruno' as an object for class 'dog'
print(bruno.bark())                    # Any attribute or methods inside the class can be called by the dot notation object.method()
print(bruno.age)                           
bruno.age=4                            # A new value can be assigned to any attribute 

"""A method can be called by two ways:
class.method(object) or object.method()
So for the above example 'bark' can be called by two different ways:"""

dog.bark(bruno)
bruno.bark()

"""A instance variable or a static variable can be called in two ways: either as an object or directly from class"""
print(bruno.legs)
print(dog.legs)
"""In order to change the static variable we have to use the class as it local to the class and not the objects"""
dog.legs=5
print(bruno.legs)



"""Encapsulation
Abstraction
Inheritance
Polymorphism"""
 
