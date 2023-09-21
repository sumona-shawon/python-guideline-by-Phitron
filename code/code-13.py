# .................... user defined function

# syntax: def name():

# 1. defining a function
def greeting():
    print("Hello, Good Morning")

# 2. function calling
greeting()

# .................... parameter and argument

def sum(a, b): # parameters: a, b
    print(f"The summation of {a} and {b} = {a+b}")

sum(2, 3) # arguments: 2, 3
sum(5, 10) # arguments: 5, 10

# .................... default parameters & keyword arguments

def greetings(name = 'Rahat', age = "23"): # default parameters
    print(f"Hello {name}. You are {age} years old.")

greetings("Kalam", 30) # overwrite default parameters

greetings(age = 23, name = 'Hamim') # keyword argument

# .................... print vs return
 
# print is fixed:
def sum(a, b):
    print(a + b)
sum(2, 3)
print(sum+5)

#return can be updated, modified:
def sum_with_return(a, b):
    return a+b # stopped
    print("Hello") # can't print after return

result = sum_with_return(2, 3)

result += 4
print(result)

print(sum_with_return(2,3)*3)