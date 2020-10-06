"""
Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
"""

def disemvowel(str1):
    newstr= str1.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')
    return newstr

str1=disemvowel("Hello name is Avi")
print(str1)

#alternate method using regular expressions 1

import re
str2="This website is for losers LOL!"
newstr2=re.sub("a|e|i|o|u|A|E|I|O|U","",str2)     #need to separate multiple characters by | in RE
print(newstr2)

#alternate method using regular expressions 2
l=['a','e','i','o','u','A','E','I','O','U']
newstr3=re.sub("|".join(l),"",str2)
print(newstr3)

#alternate method using for loop
input1="aeiouAEIOU"
newstr4=str2
for char in input1:
    newstr4=newstr4.replace(char,"")
print(newstr4)