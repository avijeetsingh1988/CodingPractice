class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other):        #This is operator overloading where we are defining what the '+' does in line 21.
        a=self.m1+other.m1
        b=self.m2+other.m2
        s3 = student(a,b)
        return s3

    def __str__(self):             
        return self.m1,self.m2
    """ We need to overload this operator becuase if we try to print and object using 'print' e.g 'print(s1)', this will only give us t
    address of the object and not the values itself. Refer line 28"""

    
s1=student(78,89)
s2=student(85,81)

s3=s1+s2                           
""" SO basically if you have to perform and operation on the objects you will have to define what the operator does first inside the 
class and this is called operator overloading. In the above example you have seen the addition operator similarly if you want to compare
the total marks for both students and see who scored higher, simply if s1>s2 will not work as '>' is not defined. The __gt__ method
will have to be defined in the class and then it will work"""

print(s3.m2)
print(s3.__str__())
"""If we only want to use 'print(s3)' then we need to convert the output of __Str__method into a string. We can do that as follows
def __str__(self):             
        return '{} {}'format.(self.m1,self.m2)
If we define the method as above then we can just print the values of the object using 'print(s3)' """