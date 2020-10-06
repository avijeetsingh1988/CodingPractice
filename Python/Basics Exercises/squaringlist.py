
def squaringlist(list):
    for i in list:
        print(i**2)

a=[4,5,6]
squaringlist(a)

#ALTERNATE WAYS TO DISPLAY THE SQUARES IN A LIST#

#1 Using append

b=[]
for number in a:
    b.append(number**2)

print(b)

#2 Using Map

d=map(lambda n:n*n,a)
print(list(d))

#3 Using for

numbers = [1, 2, 3, 4, 5]

squared_numbers = [number ** 2 for number in numbers]

print(squared_numbers)

#by creating higher order function which takes another function as its argument.

def square(x):
    return x**2

def mymap(func,arg):
    result=[]
    for i in arg:
        result.append(func(i))
    return result

squares= mymap(square,[1,2,3,4])
print(squares)
