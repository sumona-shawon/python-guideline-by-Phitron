# .................... category of function

# no argument, no return:
def greeting():
    print("Hello")
greeting()

# calculate, no parameters:
def sum():
    a = int(input("Enter a number"))
    b = int(input("Enter another number"))
    print(a + b)
sum()

# no argument, has return:
def addition():
    a = 4
    b = 3
    # a = int(input())
    # b = int(input())
    return a + b

result = addition()
print(result + 10)

# function with argument, no return:
def addition(a = 10, b = 5):
    result = print(a + b) + 10
    print(result)

addition()
addition(4, 5)

# function with argument, return value:
def juice_maker(a, b):
    res = f"mixture of {a} and {b} juice are ready"
    return res

result = juice_maker("apple", "orange")
result2 = juice_maker("banana", "orange")
print(result)
print(result2)

# .................... lamda function (anonymous function)

# normal function:
def greet():
    print("Hello, Good Morning")

# lamda function:
# a = lamda arg: expression

a = lamda : print("Hello, Good Morning")
print(a)