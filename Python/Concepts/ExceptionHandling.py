"""
What is an exception?
When the program is running and there is an error the program stops and raises an exception giving a description of the error 
and the traceback i.e where the error occured.


In python there are three types of erros:
    a) Complile Time Errors
    b) Logical Errors
    c) Run Time Errors"""

a=5
b=0
 
try:
    print(a/b)
except ZeroDivisionError:
    print("Cant divide by zero")
