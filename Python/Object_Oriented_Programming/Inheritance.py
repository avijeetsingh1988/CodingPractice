class grandparent:
    def __init__(self):
        print("Dadaji")
    def lastname(self):
        print("Gill")

class parent:
    def __init__(self):
        print("Papa")
    def lastname(self):
        print('Singh')
    def firstname(self):
        print('amrit')

class child(parent):                # This is how you define the child class, with the parent class inside the parenthesis.
    def __init__(self):
        print("me")                  
    def firstname(self):
        print("Avijeet")

mom=parent()

mom.lastname()

me=child()

"""The object of the child class inherits from the parent class so all the methods in the parent are applicable to the child class 
as well"""

me.lastname()                                                         

me.firstname()

"""A class can also inherit from two different classes. Lets say there is a grandparent class and the child class inherits from both 
the parent and grandparent"""

class child2(parent,grandparent):     # Here the class is inheriting from grandparent and parent class
    
    def __init__(self):
        super().__init__()            # This will return the __init__ value from class parent because of MRO. Look Below"
        print("sister")       
    
    def firstname(self):
        print('jeeta')

param= child2()

param.firstname()                      # The method inside the child class takes priority over the parent class. 

param.lastname()                        
"""When you run the above line the lastname methods from the parent class is called because while declaring class child2 parent was the 
first class and then came grandparent. This will change if you put grandparent first. This is called  Method Resolution Order."""