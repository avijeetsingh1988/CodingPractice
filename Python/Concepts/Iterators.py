"""An object is iterable if it can be looped over. E.g a 'list'. If you are not sure whether the object passed is iterable or not you can 
check with the 'dir' function.If the directory contains __iter__ magic method then it is iterable"""

list1=[1,2,3,4]
print(dir(list1))

list=iter(list1)
print(list)

"""This will only print the address. In order to print the output you need to pass 'next'. Note that you can only pass next to
iterators. The 'list1' is an iterable not an iterator i.e If you run 'next' directly on the 'list1' it wont work as the 'list1' does not 
have __next__ method in its directory. """

print(next(list))

"""Following we can create our own iterator using class. To create your own iterator remeber it has to have a __iter__ method and
__next__ method """
class MyRange:
    def __init__(self,start,end):
        self.start=start
        self.end=end

    def __iter__(self):
        return self

    def __next__(self):
        current=self.start
        if self.start>=self.end:
            raise StopIteration
        
        self.start +=1
        return current



coderange= MyRange(2,10)
print(next(coderange))
print(next(coderange))

""" for num in coderange:
    print(num)
 """