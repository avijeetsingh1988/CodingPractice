"""Our task is to make a function that can take any non-negative integer as a argument and return it with its digits in 
descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 21445 Output: 54421"""

num=38734
string_list = [int(i) for i in str(num)]
string_list.sort(reverse=True)
integer_list = [str(i) for i in string_list]
new_number = int("".join(integer_list))
print(new_number)

# Learnings:
# Int object is not iterable that is why we convert it to a string first so that we can convert it to a list.
# We can use sort function on iterables to sort out the data

"""Best code from code wars"""

def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))

# Learnings:
# Strings can be sorted without converting them into a list first

