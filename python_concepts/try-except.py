"""Lets us go through try and except exception handleing in python.
An Exception is a error that causes the program to crash.It is not an syntectical error,it
occurs mostly due to our negligence such as devide a number by zero , deleting an used function
name , concatinating a integer with a string are the common negligence due to which our
code crashes.
In python we have try block in which we write the code which we think an exception will occur and a
except block which is similar to catch block in other programming language which catch the 
error and let the other part of the code to execute.Lets us see try and except in action

Exception: the class name of the Exception class in Python. 
as: keyword to assign an object to a variable. e: the variable to which the Exception object is assigned to
"""

#without using try,except

print("Enter a number:") #aa
num1 = input()#aa
print("Enter another number:")#bb
num2 = input()#bb
try:
    print("The sum of the two number is :",
      int(num1)+int(num2)) #aa+bb
except  Exception as e:
    print(e)

print("The rest of the code should be handled carefully")