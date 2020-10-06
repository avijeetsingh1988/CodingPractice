def strlength(str):
    #return len(str)#
    count=0
    for length in str:
        count=count+1
    return count
print(strlength("Hello"))

#tests#
assert strlength("Avi")==3 
assert strlength("hello")!=3
print("YOUR CODE IS CORRECT")