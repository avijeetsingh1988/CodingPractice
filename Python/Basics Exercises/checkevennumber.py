def evennumber(number):
    if number%2==0: return True
    else: return False
print(evennumber(6))

#tests#
assert evennumber(2)==True
assert evennumber(101)==False
print("YOUR CODE IS CORRECT")
