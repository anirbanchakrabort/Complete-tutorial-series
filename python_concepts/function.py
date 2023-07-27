"""Function are the lines of code that can be used multiple times inside a program.There are
two types of function - build-in and user-defined. Build-in functions are already present insde
a python program and we need to call the specific function to perform some task such as sum().
User-defined functions are defined by using def keyword followed by function name and a colone
to enter inside a function. We can also use a return type if proving the arguments inside the
paranthesis if it is needed by our function.
"""

# #build-in
# a = 5
# b = 6
# c = sum((a,b))
# print(c)

#user-defined
def function(a,b):
    average = (a+b)/2
    print(average)
    return average
c = function(5,5)
print(c)
