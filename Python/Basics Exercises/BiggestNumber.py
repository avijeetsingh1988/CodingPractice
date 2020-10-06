"""This is the advanced method by using a function inside a function"""
def biggernumber(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2

def biggestnumber(num1,num2,num3):
    return biggernumber(biggernumber(num1,num2),num3)


#tests#
assert biggestnumber(9,13,15)==15
assert biggestnumber(99,0,100)==100
print("YOUR CODE IS CORRECT")