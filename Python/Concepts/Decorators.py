"""To understand decorators first we need to understand what are closures. Closures are basically inner functions that remember 
the environment they were built in and has access to variables in the local scope in which it was created even after the outer 
function has finished executing. So in the following example the wrapper function the closure."""

def decorator_func(message):
    def wrapper_func():
        print(message)
    return wrapper_func

hi_func=decorator_func('Hi')
hello_func=decorator_func('Hello')
hi_func()
hello_func()

"""A decorator is basically when a function it accepts another funcition as an argument. In the above example we have passed 
'message' variable to the 'decorator_func', but to explain decorator we will pass another function.

Decorating our functions allows us to easily add funcitonality to our existing functions by adding it in the wrapper function
"""

def decorator_func_new(originalfunc):
    def wrapper_func_new():
        return originalfunc()
    return wrapper_func_new

def display():
    print('Display func ran')

decorated_display=decorator_func_new(display)
decorated_display()

"""Now instead of line 24 and 25 we can make things simple if we use @decorator_func_new before the display function"""

@decorator_func_new                     #This is the decorator symbol
def display2():
    print("Display2 func ran")

display2()

"""If you want to pass multiple arguments to the original function then we need to pass *args,**kwargs in the wrapper function so the 
code in line 16-19 would look like:
def decorator_func_new(originalfunc):
    def wrapper_func_new(*args,**kwargs):
        return originalfunc(*args,**kwargs)
    return wrapper_func_new


"""

