def biggernumber(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2

print(biggernumber(12,20))

#tests#
assert biggernumber(13,15)==15
assert biggernumber(99,0)==99
print("YOUR CODE IS CORRECT")

"""Incase of a list you can also use the reduce function to find out
the biggest number in the List.

list=[1,5,9,3,6]
biggestnumber=reduce(lambda a,b:a if a>b else b, list)
print(biggestnumber)"""