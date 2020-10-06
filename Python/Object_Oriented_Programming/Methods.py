"""Following are the three differnt methods in OOP:
a) Instance Methods
b) Class Mehtods
c) Static Methods

The following example explains the different types of methods

"""

class student:
    school= 'Stephens'
    def __init__(self,sub1,sub2,sub3):
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
    
    def avg(self):                                          # This is the instance methods that works with instance variables
        return (self.sub1+self.sub2+self.sub3)/3

    @classmethod                                            # This is a DECORATOR that tells us the method is going to be a class method.
    def getschool(cls):                                          # This is the class methods which works with class variables.
        return(cls.school)


student1=student(78,95,87)
print(student1.avg())
print(student.getschool())